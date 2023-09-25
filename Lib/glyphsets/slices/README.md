# Google Fonts API slicing strategies

For some scripts a single subset is insufficient. In particular, for Chinese, Japanese, Korean
and emoji we need finer grained divisions. These are described using "slicing strategies."

https://www.unicodeconference.org/presentations-42/S5T3-Sheeter.pdf describes how and why these strategies
were developed.

**Please do not modify the slicing strategies here, collaborate with the Google Fonts eng team for that**

## File format

The files given here are text protos using the following proto definition:

```proto
// The slicing strategy, composed of slices.
message SlicingStrategy {
  repeated Subset subsets = 1;
}

// One subset of all codepoints.
message Subset {
  // Set of unique codepoints.
  repeated int32 codepoints = 1;
}
```