use quote::{format_ident, quote};
use std::{
    env,
    fs::{read_to_string, File},
    io::{BufWriter, Write},
    path::Path,
};

fn main() {
    let mut constants = vec![];
    let mut inserts = vec![];
    for filename in glob::glob("Lib/glyphsets/results/nam/*.nam")
        .expect("Failed to read glob pattern")
        .flatten()
    {
        let mut current_codepoints = vec![];
        let glyphset = filename
            .file_name()
            .unwrap()
            .to_str()
            .unwrap()
            .replace(".nam", "");
        read_to_string(filename).unwrap().lines().for_each(|line| {
            if line.starts_with('#') {
                return;
            }
            let mut parts = line.split_whitespace();
            let mut codepoint = parts.next().unwrap();
            if codepoint.starts_with("0x") {
                codepoint = &codepoint[2..];
            }
            let codepoint = u32::from_str_radix(codepoint, 16).unwrap();
            current_codepoints.push(codepoint);
        });
        let glyphset_uc = format_ident!("{}_CODEPOINTS", glyphset.to_uppercase());
        let codepoints = current_codepoints.len();
        let piece = quote! {
            pub const #glyphset_uc: [u32; #codepoints] = [#(#current_codepoints),*];
        };
        constants.push(piece);
    }

    // Let's add all the definitions
    for filename in glob::glob("Lib/glyphsets/definitions/*.yaml")
        .expect("Failed to read glob pattern")
        .flatten()
    {
        let glyphset = filename
            .file_name()
            .unwrap()
            .to_str()
            .unwrap()
            .replace(".yaml", "");
        let glyphset_def = format_ident!("{}_DEFINITION", glyphset.to_uppercase());
        let glyphset_codepoints = format_ident!("{}_CODEPOINTS", glyphset.to_uppercase());
        let glyphset_uc = format_ident!("{}", glyphset.to_uppercase());

        let str_contents = read_to_string(filename).unwrap();
        let piece = quote! {
            pub const #glyphset_def: &str = #str_contents;

            pub static #glyphset_uc: LazyLock<Glyphset> = LazyLock::new(|| {
                let mut def: Glyphset = serde_yaml_ng::from_str(#glyphset_def).unwrap();
                def.name = String::from(#glyphset);
                def.codepoints = #glyphset_codepoints.iter().copied().collect();
                def
            });
        };
        let insert = quote! {
            glyphsets.insert(String::from(#glyphset), #glyphset_uc.clone());
        };
        inserts.push(insert);
        constants.push(piece);
    }
    // And output
    let path = Path::new(&env::var("OUT_DIR").unwrap()).join("data.rs");
    let mut file = BufWriter::new(File::create(path).unwrap());
    let output = quote! { use std::collections::BTreeMap; use std::sync::LazyLock;

        #(#constants)*
        pub static GLYPHSETS: LazyLock<BTreeMap<String, Glyphset>> = LazyLock::new(|| {
            let mut glyphsets = BTreeMap::new();
            #(#inserts)*
            glyphsets
        });
    };
    let output_file = syn::parse_file(&output.to_string()).unwrap();
    let formatted = prettyplease::unparse(&output_file);
    // let formatted = output.to_string();

    write!(file, "{}", formatted).unwrap();
}
