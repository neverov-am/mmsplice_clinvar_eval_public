from mmsplice.vcf_dataloader import SplicingVCFDataloader
from mmsplice import MMSplice, predict_all_table
from mmsplice.utils import max_varEff

# assigning variables

ref = '../mmsplice_clinvar_eval_public/data/chr1.fa'
gtf = '../mmsplice_clinvar_eval_public/data/chr1.gtf.gz'
vcf_benign = '../mmsplice_clinvar_eval_public/data/clinvar_chr1_benign.vcf.gz'
vcf_pathogenic = '../mmsplice_clinvar_eval_public/data/clinvar_chr1_pathogenic.vcf.gz'
csv_benign = '../mmsplice_clinvar_eval_public/results/prediction_benign.csv'
csv_pathogenic = '../mmsplice_clinvar_eval_public/results/prediction_pathogenic.csv'

# running the model on benign variants

print("Running the model on benign variants...")

dl = SplicingVCFDataloader(gtf, ref, vcf_benign)
model = MMSplice()
predictions = predict_all_table(model, dl, pathogenicity=True)
predictionsMax = max_varEff(predictions)
predictionsMax.to_csv(csv_benign)

# running the model on pathogenic variants

print("Running the model on pathogenic variants...")

dl = SplicingVCFDataloader(gtf, ref, vcf_pathogenic)
model = MMSplice()
predictions = predict_all_table(model, dl, pathogenicity=True)
predictionsMax = max_varEff(predictions)
predictionsMax.to_csv(csv_pathogenic)
