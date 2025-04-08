# Native Sources
Data that do not come from filtering a bigger dataset, or prompting an LLM.

#### AIME.
US high-school competition, American Invitational Mathematics Examination.  
**Size**: 15 questions per year  
**Where to find it**: Various formatted datasets based on historical AIME questions are available, e.g., [on HuggingFace](https://huggingface.co/datasets/di-zhang-fdu/AIME_1983_2024)  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
**Current format:**  `parquet`  
**Notes**: Since AIME is an annual examination, new data becomes available each year. However, designers may select questions already present on the internet, which could be included in pretraining corpora.  

#### AMC.
American Math competition for various high-school students, which acts as a pre-selection to AIME.  
**Size**: 3 (levels) times 25 multi-choice questions per year.  
**Where to find it**: Various formatted datasets based on historical AMC questions are available, e.g. https://huggingface.co/datasets/AI-MO/aimo-validation-amc/  

#### ArXiv.
**Current format:**  `jsonl.zst`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
**Size**: 29B tokens  
**Where to find it**: https://huggingface.co/datasets/EleutherAI/proof-pile-2 contains data scrapped from the ArXiv website, according to a snapshot taken in 2023 by RedPajama.  
**Notes**: The dataset is valuable for training models on advanced mathematical concepts and research-level problems.  

#### CodeForces.
**Current format:**  `parquet`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
Website with competitive programming puzzles.  
**Size**: 700,000 samples, 1.7 GB  
**Where to find it**: https://huggingface.co/datasets/MatrixStudio/Codeforces-Python-Submissions  
**Notes**: Quite extensive datasets with unit test  

#### GSM8k.
**Current format:**  `jsonl`  
**Current location:**  `/checkpoint/amaia/explore/datasets/evals`.  
Grade School Math (GSM) benchmark, created by human annotator for OpenAI.  
**Size**: 8,500 problems, 5 MB  
**Where to find it**: https://github.com/openai/grade-school-math  
**Companion paper**: https://arxiv.org/abs/2110.14168  

#### LeetCode.
**Current format:**  `jsonl`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
Website with programming puzzles, typically used to prepare coding interviews.  
**Size**: 2,000 samples, 7 MB (for the small version I found on HuggingFace)  
**Where to find it**: https://huggingface.co/datasets/greengerong/leetcode  
**Notes**: Unclear how the dataset was collected, comes with no unit tests  

#### MBPP (Mostly Basic Python Problems).
**Current location**: `/checkpoint/amaia/explore/datasets/evals`.  
Crowd-sourced datasets of small Python problems  
A dataset consisting of 1,000 Python programming problems aimed at entry-level programmers.  
**Size**: 1,000 samples  
**Where to find it**: https://github.com/google-research/google-research/tree/master/mbpp  
**Companion paper**: https://arxiv.org/abs/2108.07732  

#### OlympiadBench.
**Current format:**  `parquet`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
Datasets collected from Olympiads with figures (multi-modal), rationale (derived by humans), various level of difficulty.  
**Size**: 8,000 questions.  
**Where to find it**: https://huggingface.co/datasets/Hothan/OlympiadBench  
**Companion paper**: https://arxiv.org/pdf/2402.14008  

#### Various Websites.
- The art of problem solving (https://artofproblemsolving.com/): a website that prepare students to various STEM competition, and is often used by researchers to craft datasets with rationale.
- ProofWiki (https://proofwiki.org/):  a website that aim at collecting math proofs.
- StackExchange
- Wikipedia

# Semi-Native Sources  
Data that was built by leveraging existing assets with substantial data scrapping work.  

#### Algebraic Stack.
**Current format:**  `jsonl.zst`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
Subset of ProofPile-2. Obtained by filtering GitHub for Coq, Isabelle, Lean and Matlab, extracting data from Mathlib 4 (the Lean library), building a dataset of Isabelle proofs, and filtering the Stack.  
**Size**: 3,000,000, 11MB.  
**Where to find it**: https://huggingface.co/datasets/EleutherAI/proof-pile-2  
**Companion paper**: https://arxiv.org/abs/2310.10631  

#### APPS.
**Current format:**  `parquet`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
10,000 programming problems with python solutions and test cases for correctness.  Curated from Codewars, AtCoder, Kattis, and Codeforces.  
**Example**: Problem about binary words with test inputs/outputs and a Python solution.   
**Size**: 10,000 problems  
**Where to find it**: https://huggingface.co/datasets/codeparrot/apps   
**Companion paper**: https://arxiv.org/pdf/2105.09938  
**Notes**: AlphaCode mentions that test coverage was insufficient, leading to false positive.  

#### AQuA (Algebra Question Answering).
**Current format:**  `parquet`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
DeepMind Dataset built by extracting 34,000 questions from undergrad, and grad student admission test (GMAT and GRE), with answer and rational scrapped on the web. Plus crowdsourcing to provide similar questions.  
**Size**: 98,000 samples; 52 MB   
**Where to find it**: https://huggingface.co/datasets/deepmind/aqua_rat  
**Companion paper**: https://arxiv.org/pdf/1705.04146  

#### CodeContests.
**Current format:**  `parquet`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
Dataset used for AlphaCode. Competitive programming problems from Aizu, AtCoder, CodeChef, Codeforces and HackerEarth.  
**Size**: 13,000 samples, 2GB  
**Where to find it**: https://huggingface.co/datasets/deepmind/code_contests  
**Companion paper**: https://arxiv.org/abs/2203.07814  
**Notes**: Includes correct and incorrect solutions. Rich data for training/debugging models.  

#### OmniMath.
**Current format:**  `jsonl`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
Data obtained from regional to international Olympiads, from the art-of-problem solving.  
**Size**: 4,000, 7 MB.  
**Where to find it**: https://huggingface.co/datasets/KbsdJames/Omni-MATH  
**Companion paper**: https://arxiv.org/abs/2410.07985  

#### Stack V2.
Scrapping of the Software Heritage archive, which contains software source code, in September 2023.  
**Size**: 5,500,000,000 samples, 67 TB  
**Where to find it:** https://huggingface.co/datasets/bigcode/the-stack-v2  

#### SWE-bench.
Datasets of codebase, issues and unit tests. The goal is to fix the codebase that currently yield the issue resulting in failing unit tests.  
The data was collected from popular Github repository.  
**Size**: 2,300 samples  
**Where to find it**: https://github.com/swe-bench/SWE-bench  
**Companion paper**: https://arxiv.org/abs/2310.06770  

#### TACO.
**Current format:**  `json`  
**Current location:**   `/checkpoint/amaia/explore/datasets/evals`.  
Algorithmic problems collected from various platforms such as CodeChef, CodeForces, HackerRank, and GeeksforGeeks, as well as existing datasets such as APPS, CodeContest, and Description2code. Each problems come with unit tests that allows to test for correctness.  
**Size**: 26,000 problems with 1.5M solutions, .   
**Where to find it**: https://huggingface.co/datasets/BAAI/TACO  
**Companion paper**: https://arxiv.org/abs/2312.14852  

# Filtered Sources
Data that come from filtering a bigger dataset.  

#### DataComp-LM (DCLM).
Filtering of Common Crawl based on heuristic cleaning and filtering (see RefinedWeb), deduplication (through Bloom), filtering with fastText classifier to match the reddit channel ExplainLikeImFive, and an instruct model.  
**Size**: 4T token
**Where to find it**: https://huggingface.co/datasets/mlfoundations/dclm-baseline-1.0
**Companion paper**: https://arxiv.org/abs/2406.11794

#### DeepSeek Math Corpus.
Filtering of Common Crawl based on a FastText classifier based on OpenWebMath as initial positive examples, and additional heuristics. Datasets not available.  
**Companion paper**: https://arxiv.org/pdf/2402.03300  

#### FineMath.
**Current format:**  `parquet`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
Filtered from CommonCrawl by HuggingFace for SmolLM focused on Math domain.  
**Size:** 48,000,000 samples, 150 GB  
**Where to find it**: https://huggingface.co/datasets/HuggingFaceTB/finemath  
**Companion paper**: https://arxiv.org/abs/2502.02737  

#### FineWeb.
Filtered from CommonCrawl by HuggingFace, seems to be slightly worse than DCLM.  
**Size:** 25,000,000,000 samples, 53 TB  
**Where to find it**: https://huggingface.co/datasets/HuggingFaceFW/fineweb  
**Companion paper**: https://arxiv.org/abs/2406.17557  

#### FineWeb-Edu.
Filtered from FineWeb to focus on sample with educational value  
**Size:** 3,000,000,000 samples, 10 TB  
**Where to find it**: https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu  
**Companion paper**: https://arxiv.org/abs/2406.17557  

#### OpenWebMath.
Filtering of CommonCrawl done in 2023, that is considered good quality.  
Not donwloaded, as FineMath is more recent.  
**Size**: 6,300,000 samples, 27 GB.  
**Where to find it**: https://huggingface.co/datasets/open-web-math/open-web-math  
**Companion paper**: https://arxiv.org/abs/2310.06786  

#### Stack-Edu.
**Current format:**  `parquet`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw` (python parts only)  
Filtering version of the Stack V2.  
**Size**: 167,000,000 samples, ~1 TB  
**Where to find it**: https://huggingface.co/datasets/HuggingFaceTB/stack-edu  
**Companion paper**: https://arxiv.org/abs/2502.02737  
**Notes**: Need to be download with S3, still really big in terms of number of tokens.  

# LLM Augmented Source
Data being synthesized with LLMs. The LLM can be used to synthesize texts or questions (usually providing example of questions from existing datasets). It can also be used to synthesize a rationale to answer questions. The answer may be verified, either with parser checking for numerical equality (i.e. `\frac13` = `0.333`), or using LLM as a judge.  
Synthesized questions (bootstrapped from existing one), synthesized, eventually verified, answers.  

#### Camel.
Exercise textbooks synthetically generated by GPT-4  
**Size:** 20,000 samples, 300 MB  
**Where to find it**L https://huggingface.co/datasets/camel-ai/physics  
**Companion paper**: https://arxiv.org/abs/2303.17760  
**Notes**: Comes with no verification of correctness  

#### GlaiveAI.
Traces from DeepSeek R1  
**Size**: 20 million examples, 87 GB  
**Where to find it**: https://huggingface.co/datasets/glaiveai/reasoning-v1-20m  
**Notes**: Comes with no verification of correctness  

#### Natural Reasoning.
From Fair RAM group, questions filtered from DCLM and FineMath, with answers provided by Llama.  
**Size:** 2,000,000 samples, 2GB  
**Where to find it**: https://huggingface.co/datasets/facebook/natural_reasoning  
**Companion paper**: https://arxiv.org/abs/2502.13124  

#### MetaMathQA.
**Current format:**  `jsonl`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
Datasets collected by "bootstrapping" gsm8k and Math  
**Size**: 400,000 samples, 200 MB.  
**Where to find it**: https://huggingface.co/datasets/meta-math/MetaMathQA   
**Companion paper**: https://arxiv.org/abs/2309.12284  
**Notes**: OpenMathInstruct is a more recent iteration of the same idea.  

#### Nemotron Post-Training Dataset v1.
**Current format:**  `json`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
We do not have too many details on this datasets, it seems to have been curated from Llama, Qwen and DeepSeek answers.  
**Size**: 15,000,000 samples, 6 GB.  
**Where to find it**: https://huggingface.co/datasets/nvidia/Llama-Nemotron-Post-Training-Dataset-v1  
**Companion paper**: https://arxiv.org/abs/2502.00203  
**Notes**: Developed to fine-tune models for improved accuracy and reliability.  

#### Numina-Tool.
**Current format:**  `parquet`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
Subset numina problems solved with tool-use.  
**Size**: 70,000 samples, 150 MB  
**Where to find it**: https://huggingface.co/datasets/AI-MO/NuminaMath-TIR  
**Companion paper**: https://arxiv.org/pdf/2309.17452  

#### OpenMathInstruct-v2.
**Current format:**  `parquet`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
Augmentation of MATH and GSM8K from LLM (rephrase questions, provide answers).  
**Size**: 22,000,000 samples, 12 GB  
**Where to find it**: https://huggingface.co/datasets/nvidia/OpenMathInstruct-2  
**Companion paper**: https://arxiv.org/abs/2410.01560  

#### Open-R1-220k.
**Current format:**  `parquet`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
This part of an ongoing effort by HuggingFace to reproduce DeepSeek R1. Consists of DeepSeek R1 traces answering problems from NuminaMath, verified with Math Verify, a HuggingFace parser to check numerical equality.  
**Size**: 225,000 samples, 8 GB.  
**Where to find it**: https://huggingface.co/datasets/open-r1/OpenR1-Math-220k  
**Notes**: They have other datasets, see https://huggingface.co/open-r1  

#### PRM800K.
Datasets created by OpenAI by using LLMs to answer question from the MATH datasets, with rationale graded by humnas.  
**Size**: 800,000 samples,   
**Where to find it**: https://github.com/openai/prm800k  
**Companion paper**: https://arxiv.org/abs/2305.20050  
**Notes**: Some annotations were reported to be incorrect  

#### Still long format.
**Current format:**  `parquet`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
Similar to Still, with a focus on long answer, questions come from NuminaMath, Aime, Leetcode, OpenCoder, Camel, Gaokao (Chinese A-level) and RiddleSense.  
**Size**: 5,000 samples, 20 MB.  
**Where to find it**: https://huggingface.co/datasets/RUC-AIBOX/long_form_thought_data_5k  
**Companion paper**: https://arxiv.org/abs/2412.09413  

# Formal Math  

#### CoqGym.
Large-scale dataset compiled from various 71,000 Coq projects.  
**Size**: 70,000 proof steps  
**Where to find it**: https://github.com/princeton-vl/CoqGym  
**Companion paper**: https://arxiv.org/abs/1905.09381  

#### DeepSeek-Prover-V1.
**Current format:**  `jsonl`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
Synthetic dataset of Lean proofs generated by DeepSeek, solving half of miniF2F.   
**Size**: 27,000 samples, 6 MB  
**Where to find it**: https://huggingface.co/datasets/deepseek-ai/DeepSeek-Prover-V1  
**Companion paper**: https://arxiv.org/abs/2405.14333  

#### IMO-Steps.
DOWNLOADED IN `/checkpoint/amaia/explore/datasets/reasoning/raw`  
20 Lean proofs of IMO problems  
**Size**: 20 samples, 6 kB  
**Where to find it**: https://huggingface.co/datasets/roozbeh-yz/IMO-Steps  
**Companion paper**:  https://arxiv.org/abs/2411.18872  

#### Isabelle Premise Selection.
Datasets of proofs in Isabelle collected from the Archive of Formal Proofs (https://www.isa-afp.org/). Useful to study premise selection (i.e. selecting potential lemmas to apply mid-proof).  
**Size**: 4,000,000 samples  
**Where to find it**: https://huggingface.co/datasets/Simontwice/premise_selection_in_isabelle  
**Companion paper**: none, but the datasets was key to https://arxiv.org/abs/2303.04488  

#### Lean-Workbook.
DOWNLOADED IN `/checkpoint/amaia/explore/datasets/reasoning/raw`  
Tens of thousands of math problems formalized in Lean4  
**Size**: 25,000 samples, 5MB  
**Where to find it**: https://huggingface.co/datasets/internlm/Lean-Workbook  
**Companion paper**: https://arxiv.org/abs/2411.18872  

#### MiniF2F.
MiniF2F is a benchmark for formal mathematics, created by Kunhao, consisting of 500 Olympiad-level mathematics problems from competitions like AIME, AMC, and IMO. Each problem is provided with both informal and formal statements.   
**Size**: 500 examples with Lean formal statements and informal statements and proofs.   
**Where to find it**: https://github.com/facebookresearch/miniF2F   
**Companion paper**: https://arxiv.org/abs/2109.00110  

# Compilation  

#### DeepScaleR.
**Current format:**  `json`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
Compiled from Aime, AMC, Omni-Math and Still  
Compilation of data from AIME, AMC, Omni-Math, and Still. Used to reproduce R1.  
**Where to find it:** https://huggingface.co/datasets/agentica-org/DeepScaleR-Preview-Dataset  
**Size:** 40,000 examples, 10 MegaBytes  

#### Eurus-RL.
**Current format:**  `parquet`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
Collection of question with verifiable answer extracted from Numina, Apps, CodeContests, Taco and Codeforces.  
**Example**: Various datasets related to reinforcement learning tasks.  
**Size**: 500,000 samples, 2 GB  
**Where to find it**: https://huggingface.co/datasets/PRIME-RL/Eurus-2-RL-Data  
**Notes**: Includes multiple datasets with corresponding training recipes.  
https://arxiv.org/abs/2502.01456  
#### Lila.
Compilation of many datasets including addsub, amps, apps, asdiv, conala, mathematics, dolphin, draw, gsm8k, math, mathqa, mbpp, mctaco, multiarith, numersense, numglus, simuleq, singleop, singleq, svamp.  
**Where to find it**: https://huggingface.co/datasets/allenai/lila  
**Companion paper**: https://arxiv.org/abs/2210.17517  
**Notes**: The datasets were collected for evaluation, it seems small and outdated.  

#### MATH.
**Current format:**  `jsonl`  
**Current location:**  `/checkpoint/amaia/explore/datasets/evals`  
Classical evaluation datasets, created by Dan Hendrycks, by collecting various US high-school competition problems with solution.  
**Size**: 12,500 samples  
**Where to find it**: https://github.com/hendrycks/math (was taken down from HuggingFace due to copyright issue filled by the art of problem solving).  
**Companion paper**: https://arxiv.org/abs/2103.03874  

#### MathInstruct.
**Current format:**  `jsonl`  
**Current location:**  `/checkpoint/amaia/explore/datasets/evals`  
A compilation of datasets (gsm8k, aqua,camel) with rationale (some of them being generated by LLMs) used to train MAmmoTH  
**Size**: 262,000 samples, 200 MB  
**Where to find it**: https://huggingface.co/datasets/TIGER-Lab/MathInstruct  
**Companion paper**: https://arxiv.org/pdf/2309.05653  

#### MathPile.
**Current format:**  `jsonl.gz`  
**Current location:**  `/checkpoint/amaia/explore/datasets/evals`  
Dataset collected by GAIR (the lab behind LIMO) by compiling textbook, arXiv, ProofWiki, and filtering common crawl.  
**Size**: Approximately 9.5 billion tokens.  
**Where to find it**: https://huggingface.co/datasets/GAIR/MathPile  
**Companion paper**: https://arxiv.org/abs/2312.17120  

#### NuminaMath.
**Current format:**  `parquet`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
Mix of math problems solved with rationale.  
Sources: aops_forum (https://artofproblemsolving.com/), amc_aime, Chinese k12, gsm8k, math, Olympiads, Orca-math (https://arxiv.org/abs/2402.14830), synthetic_amc, synthetic_math  
**Size**: Approximately 900,000 samples, 531 MB.  
**Where to find it**: https://huggingface.co/datasets/AI-MO/NuminaMath-1.5  

#### Proof-Pile-2.
**Current format:**  `jsonl.zst`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
Massive pretraining corpus of formal mathematics and related documents (Lean, Coq, math papers).  
**Size**: 60B tokens,  
**Where to find it**: https://huggingface.co/datasets/EleutherAI/proof-pile-2  
**Companion paper**: https://arxiv.org/abs/2310.10631  

#### Still.
**Current format:**  `parquet`  
**Current location:**  `/checkpoint/amaia/explore/datasets/reasoning/raw`  
Collection of question and verifiable answer extracted from Math, Numina, and Aime.  
**Size**: 30,000 samples, 10 MB  
**Where to find it**: https://huggingface.co/datasets/RUC-AIBOX/STILL-3-Preview-RL-Data  
**Companion paper**: https://arxiv.org/abs/2412.09413  
  

# Additional notes (for additional assets)

MIT-8 benchmark

Proof-Pile
- ArXiv.math (10GB)
- Open-source math textbooks (50MB)
- Formal mathematics libraries (500MB)
    - Lean mathlib and other Lean repositories
    - Isabelle AFP
    - Coq mathematical components and other Coq repositories
    - HOL Light
    - set.mm
    - Mizar Mathematical Library
- Math Overflow and Math Stack Exchange (2.5GB)
- Wiki-style sources (50MB)
    - ProofWiki
    - Wikipedia math articles
- MATH dataset (6MB)


Make some card for generic ressources.
- Educational website
- Formal proof repositories
    - Isabelle AFP