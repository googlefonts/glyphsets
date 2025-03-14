use std::collections::{HashMap, HashSet};

use serde::Deserialize;

use thiserror::Error;

#[derive(Debug, Error)]
pub enum GlyphsetError {
    #[error("Glyphset not found")]
    GlyphsetNotFound,
    #[error("Bug in glyphset definitions")]
    InternalInconsistency,
}

fn script_name(s: &str) -> String {
    // We could do this properly but we only have a few scripts, so:
    match s {
        "Latn" => "Latin".to_string(),
        "Arab" => "Arabic".to_string(),
        "Cyrl" => "Cyrillic".to_string(),
        _ => s.to_string(),
    }
}

include!(concat!(env!("OUT_DIR"), "/data.rs"));

#[derive(Default, Debug, Clone, Deserialize, PartialEq)]
/// The definition of a glyph set used by Google Fonts
pub struct Glyphset {
    #[serde(skip)]
    name: String,
    #[serde(default)]
    description: String,
    #[serde(default)]
    include_glyphsets: Vec<String>,
    #[serde(default)]
    language_codes: Vec<String>,
    #[serde(skip)]
    codepoints: HashSet<u32>,
    use_auxiliary: Option<bool>,
    historical: Option<bool>,
    #[serde(default)]
    regions: Vec<String>,
    #[serde(default)]
    exclude_language_codes: Vec<String>,
    population: Option<u32>,
}

impl Glyphset {
    fn script(&self) -> String {
        self.name
            .split("_")
            .skip(1)
            .take(1)
            .next()
            .expect("Malformed glyphset name - no script")
            .to_string()
    }
}

/// A struct to hold coverage information for a single glyphset
#[derive(Default, Debug, Clone)]
pub struct Coverage {
    /// The set of codepoints from the glyphset present in the provided codepoint set
    pub has: HashSet<u32>,
    /// The set of codepoints from the glyphset which are not present in the provided codepoint set
    pub missing: HashSet<u32>,
    /// The fraction of the glyphset present (0.0 to 1.0)
    pub fraction: f32,
}

pub fn get_coverage<T>(codepoints: &T, glyphset: &str) -> Option<Coverage>
where
    for<'a> &'a T: IntoIterator<Item = &'a u32>,
{
    let codepoints_set: HashSet<u32> = codepoints.into_iter().copied().collect();
    GLYPHSETS.get(glyphset).map(|gs| {
        let our_codepoints = &gs.codepoints;
        let mut coverage = Coverage::default();
        let our_codepoints_set: HashSet<u32> = our_codepoints.iter().copied().collect();
        coverage.has = our_codepoints_set
            .intersection(&codepoints_set)
            .copied()
            .collect();
        coverage.missing = our_codepoints_set
            .difference(&codepoints_set)
            .copied()
            .collect();
        // Percentage calculations are a little involved...
        if !coverage.has.is_empty() && coverage.missing.is_empty() {
            coverage.fraction = 1.0;
        } else if glyphset == "GF_Latin_Core" || glyphset == "GF_Latin_Kernel" {
            coverage.fraction = coverage.has.len() as f32 / our_codepoints.len() as f32;
        } else {
            let our_codepoints_without_core = our_codepoints_set
                .difference(&GF_LATIN_CORE_CODEPOINTS.into())
                .copied()
                .collect::<HashSet<_>>();
            let our_codepoints_without_kernel = our_codepoints_set
                .difference(&GF_LATIN_KERNEL_CODEPOINTS.into())
                .copied()
                .collect::<HashSet<_>>();
            let unicodes_unique_in_glyphset =
                if our_codepoints_without_core.is_superset(&our_codepoints_without_kernel) {
                    our_codepoints_without_core
                } else {
                    our_codepoints_without_kernel
                };
            if unicodes_unique_in_glyphset.is_empty() {
                coverage.fraction = 0.0;
            } else {
                let has = coverage
                    .has
                    .intersection(&unicodes_unique_in_glyphset)
                    .count();
                coverage.fraction = has as f32 / unicodes_unique_in_glyphset.len() as f32;
            }
        }
        coverage
    })
}

pub fn get_glyphset_coverage<T>(codepoints: &T) -> HashMap<String, Coverage>
where
    for<'a> &'a T: IntoIterator<Item = &'a u32>,
{
    GLYPHSETS
        .keys()
        .map(|glyphset| {
            let coverage = get_coverage(codepoints, glyphset).unwrap();
            (glyphset.to_string(), coverage)
        })
        .collect()
}

pub fn languages_per_glyphset(gs: &str) -> Result<Vec<String>, GlyphsetError> {
    let glyphset = GLYPHSETS.get(gs).ok_or(GlyphsetError::GlyphsetNotFound)?;
    let mut codes = glyphset.language_codes.clone();
    for include in &glyphset.include_glyphsets {
        let include_glyphset = GLYPHSETS
            .get(include)
            .ok_or(GlyphsetError::InternalInconsistency)?;
        codes.extend(include_glyphset.language_codes.clone());
    }
    if !glyphset.regions.is_empty() {
        for language in google_fonts_languages::LANGUAGES.values() {
            if glyphset
                .exclude_language_codes
                .contains(&language.id().to_string())
            {
                continue;
            }
            if language.historical() && !glyphset.historical.unwrap_or(false) {
                continue;
            }
            // Why did I make language.population signed? That's just not smart.
            if glyphset.population.unwrap_or(0) as i32 > language.population() {
                continue;
            }
            if glyphset.script() == script_name(language.script()) {
                let language_region_set: HashSet<_> = language.region.iter().collect();
                if glyphset
                    .regions
                    .iter()
                    .any(|region| language_region_set.contains(region))
                {
                    codes.push(language.id().to_string());
                }
            }
        }
    }
    Ok(codes)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_name() {
        assert!(languages_per_glyphset("GF_Arabic_Plus").unwrap().len() >= 8);
        assert!(languages_per_glyphset("GF_Latin_African").unwrap().len() >= 617);
    }
}
