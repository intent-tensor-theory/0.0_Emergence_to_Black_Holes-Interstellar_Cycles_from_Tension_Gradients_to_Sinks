#!/bin/bash
# PDF Build Script for Emergence Book
# Uses pandoc with LaTeX backend

# Configuration
OUTPUT_DIR="output"
BOOK_NAME="emergence_framework"
CHAPTERS_DIR="chapters"
APPENDICES_DIR="appendices"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Chapter order
CHAPTERS=(
    "00_preface.md"
    "01_pre-geometric-domain.md"
    "02_gradient-formation.md"
    "03_curl-and-memory.md"
    "04_boundary-closure.md"
    "05_selection-laws.md"
    "06_ichtb-diagnostics.md"
    "07_pre-atomic-emergence.md"
    "08_atomic-lock-in.md"
    "09_nebular-case-studies.md"
    "10_galactic-persistence.md"
    "11_collapse-boundaries.md"
    "12_synthesis.md"
)

APPENDICES=(
    "A_mathematical.md"
    "B_domain-mappings.md"
    "C_observational.md"
    "D_computational.md"
    "E_falsifiability.md"
    "F_open-questions.md"
)

# Build chapter list with paths
CHAPTER_FILES=""
for ch in "${CHAPTERS[@]}"; do
    CHAPTER_FILES="$CHAPTER_FILES ../$CHAPTERS_DIR/$ch"
done

APPENDIX_FILES=""
for app in "${APPENDICES[@]}"; do
    APPENDIX_FILES="$APPENDIX_FILES ../$APPENDICES_DIR/$app"
done

# Build full PDF
echo "Building full PDF..."
cd "$OUTPUT_DIR"

pandoc \
    --from=markdown \
    --to=pdf \
    --pdf-engine=xelatex \
    --toc \
    --toc-depth=3 \
    --number-sections \
    -V geometry:margin=1in \
    -V fontsize=11pt \
    -V documentclass=report \
    -V title="The Matter of Emergence" \
    -V subtitle="A Gradient-Based Framework for the Formation of Structure from Quantum to Cosmic Scales" \
    -V author="Armstrong Knight" \
    -V date="$(date +%Y)" \
    -o "${BOOK_NAME}_full.pdf" \
    ../README.md \
    $CHAPTER_FILES \
    $APPENDIX_FILES

echo "Done: $OUTPUT_DIR/${BOOK_NAME}_full.pdf"

# Build chapters-only PDF
echo "Building chapters-only PDF..."
pandoc \
    --from=markdown \
    --to=pdf \
    --pdf-engine=xelatex \
    --toc \
    --toc-depth=2 \
    --number-sections \
    -V geometry:margin=1in \
    -V fontsize=11pt \
    -V documentclass=report \
    -o "${BOOK_NAME}_chapters.pdf" \
    $CHAPTER_FILES

echo "Done: $OUTPUT_DIR/${BOOK_NAME}_chapters.pdf"

cd ..
echo "Build complete."
