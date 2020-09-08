# Evaluation of MMSplice pathogenicity scores on ClinVar Chr1

## Content:
- data/:
  - chr1.fa(.fai): chr1 reference sequence
  - chr1.gtf.gz: Ensembl reference annotation
  - clinvar_chr1_[benign|pathogenic].vcf.gz(.tbi): ClinVar variants on chromosome 1


## Task: Analyse the association between MMSplice pathogenicity scores and benign vs. pathogenic ClinVar variants

0) fork this repository
1) call `tar -xjvf data.tar.gz`
2) create `run_mmsplice.py` script: Apply MMSplice to the ClinVar variants. (This can take 5-10min.)
3) create a Jupyter notebook to analyse the differences in MMSplice predictions between benign and pathogenic ClinVar variants.
Provide at least a convincing plot that compares the pathogenicity scores between benign and pathogenic variants.
4) Publish your results on github


