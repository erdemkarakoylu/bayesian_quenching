### Monopaper layout

npq-bayes/
  paper1_methods/
    analysis/   # notebooks or scripts
    model/      # PyMC model code
    figs/       # saves
    paper/      # Quarto or Overleaf export
  paper2_science/
    analysis/
    model/
    figs/
    paper/
  data/README.md  # pointers to EDI/your files, not raw large data
  env/environment.yml
  makefile  # `make reproduce` for each paper
  LICENSE
  CITATION.cff

Round 1 — Methods (Lake George only)

1a. Preprint (EarthArXiv)

Title (working): A Bayesian NPQ-correction workflow for in-situ chlorophyll fluorescence: a Lake George demo.

Contents to lock:

Problem framing + DAG (your latest v3).

Data: Lake George file, variables, units, QC; note zero missingness.

Model: joint log-scale formulation (predict 
𝐹
chl
F
chl
	​

 & 
𝐹
ref
F
ref
	​

; infer 
𝜃
θ=NPQ-free and 
𝛿
δ=NPQ state).

Priors: unit-aware (no data standardization), prior-predictive checks.

Validation: posterior predictive, coverage, LOO-PIT, Δ-model baseline, deterministic NPQ correction comparison.

Reproducibility: repo with env.yml, make reproduce, data pointers, and a lightweight README “how to run.”

1b. Submit to Limnology & Oceanography: Methods (hybrid, non-OA)

Keep it methods-first: clarity, diagnostics, and deployment guidance (how to set unit-aware priors in practice).

Figures/tables (suggested):

F1 DAG (v3).

F2 Lake George EDA (diurnal cycles; irradiance/depth/temperature).

F3 Δ vs log-irradiance with partial pooling by site.

F4 Posterior predictive checks for 
𝐹
chl
F
chl
	​

, 
𝐹
ref
F
ref
	​

.

F5 Calibration: coverage & LOO-PIT (2-panel).

F6 Counterfactuals: vary irradiance/depth; show 
𝛿
δ and 
𝜃
θ.

T1 Priors (interpretation by “meaningful step size”).

T2 Model comparison (joint vs Δ-model), predictive & calibration metrics.

T3 Sensitivity (priors, link choices).

Data & code availability statements: point to the preprint repo; include a tagged release/DOI.