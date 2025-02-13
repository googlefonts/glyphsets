use std::collections::{HashMap, HashSet};

include!(concat!(env!("OUT_DIR"), "/data.rs"));

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
    GLYPHSETS.get(glyphset).map(|our_codepoints| {
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
                .difference(&GF_LATIN_CORE.into())
                .copied()
                .collect::<HashSet<_>>();
            let our_codepoints_without_kernel = our_codepoints_set
                .difference(&GF_LATIN_KERNEL.into())
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
