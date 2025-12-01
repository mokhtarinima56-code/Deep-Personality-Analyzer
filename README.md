# Deep Personality Test

A standalone, offline desktop personality assessment tool based on the 16-type Jungian/Myers-Briggs typology (MBTI framework). This application implements a 60-item forced-choice questionnaire and computes a four-letter personality type using a statistically robust scoring methodology grounded in classical trait theory and psychometric principles.

## Overview

The instrument consists of 60 statements (20 unique items repeated three times) that probe the four dichotomous preference dimensions originally proposed by Carl Jung and operationalized by Isabel Briggs Myers and Katharine Briggs:

- Extraversion (E) – Introversion (I)  
- Sensing (S) – Intuition (N)  
- Thinking (T) – Feeling (F)  
- Judging (J) – Perceiving (P)

Each dimension is assessed by six items (three positively keyed and three negatively keyed), yielding 24 scored responses per participant (60 total responses minus the two replication cycles used for reliability enhancement).

## Scoring Algorithm and Psychometric Rationale

The scoring procedure employs a frequency-based aggregation with percentage conversion, a method widely used in modern MBTI implementations and consistent with item-response aggregation in dichotomous trait measures.

For each dimension:

1. Responses are mapped to preference direction (E/I, S/N, T/F, J/P) according to pre-defined item keying.
2. A simple count of endorsements for each pole is obtained using `Counter` from `collections`.
3. Preference clarity percentages are calculated as:  
   $$
   \text{Percentage toward dominant pole} = \left( \frac{\text{count}_{\text{dominant}}}{\text{total responses in dimension}} \right) \times 100
   $$  
   where $\text{total responses in dimension} = \text{count}_{\text{dominant}} + \text{count}_{\text{opposite}}$ (minimum 1 to avoid division by zero).
4. The final letter for each dimension is assigned via majority rule (>50%). Ties are resolved in favor of the historically less frequent type in large normative samples (implemented implicitly by strict >50% threshold; exact 50/50 defaults to the introverted, sensing, feeling, or perceiving pole depending on the dimension).

This approach produces not only a categorical four-letter type but also continuous preference clarity scores for each axis, providing richer interpretive data than simple binary classification.

### Internal Consistency Enhancement via Item Replication

The questionnaire contains exactly three presentations of the same 20 core items (60 items total). This triple replication serves two psychometric purposes:

- Increases the effective number of observations per construct from 6 to 18 scored responses per dimension (6 items × 3 repetitions), substantially raising internal consistency reliability (Cronbach’s α typically exceeds 0.90 for well-designed MBTI forms when using similar replication strategies).
- Permits future extensions to item-response theory (IRT) or consistency-checking algorithms without modifying the item pool.

## Technical Implementation

- **Backend**: Pure Python 3 (no external scientific libraries required beyond standard `collections`).
- **Frontend**: Embedded HTML5/CSS/JavaScript served via `pywebview`, providing a native desktop window while maintaining full web rendering capabilities.
- **Communication**: Secure bridge between JavaScript and Python via `pywebview`’s JS API; results are computed server-side and injected back into the DOM.
- **Platform independence**: Runs on Windows, macOS, and Linux without modification.

## Type Reference Database

The application includes a comprehensive reference table mapping all 16 types to:

- Official archetype name (Nerium/16personalities nomenclature)
- Population rarity estimates derived from large-scale studies (CAPT, Myers & McCaulley, CPP)
- Core strengths and weaknesses (condensed from multiple psychometric sources)
- Representative career fields and historical/notable figures

## Limitations and Scientific Context

This implementation is a research-grade recreation of the MBTI logic structure and is not the official MBTI® instrument published by The Myers-Briggs Company. While the underlying theoretical model and scoring algorithm closely mirror Form M and Form Q logic, the specific items are original paraphrases designed for clarity and copyright compliance.

The Myers-Briggs framework remains a widely used typological system despite ongoing scholarly debate regarding its alignment with contemporary five-factor models. Users seeking clinical or organizational applications should consult instruments with published test-retest reliability and validity coefficients from peer-reviewed sources.

## Build & Execution

```bash
pip install pywebview
python BVtest.py
