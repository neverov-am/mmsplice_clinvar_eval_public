# Evaluation of MMSplice pathogenicity scores on ClinVar Chr1

Content:
- data/:
  - chr1.fa(.fai): chr1 reference sequence
  - chr1.gtf.gz: Ensembl reference annotation
  - clinvar_chr1_[benign|pathogenic].vcf.gz(.tbi): ClinVar variants on chromosome 1


## Task: Vizualize the differences in pathogenicity scores between benign and pathogenic variants

0) fork this repository
1) call `tar -xjvf data.tar.gz`
2) create `run_mmsplice.py` script: Run MMSplice on benign and pathogenic variants.
3) create a Jupyter notebook to vizualize the differences in pathogenicity scores between benign and pathogenic variants.
4) Publish your Jupyter notebook on github


