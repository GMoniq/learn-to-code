import os, pathlib, sys
from urllib import request

import scanpy as sc
#import scvi
import numpy as np
import pandas as pd

anndata_path = "https://cellgeni.cog.sanger.ac.uk/developmentcellatlas/fetal-immune/PAN.A01.v01.raw_count.20210429.HSC_PROGENITORS.embedding.h5ad"
download_path = "../../data/processed/hsc_progenitors.h5ad"
request.urlretrieve(anndata_path, download_path)

ad = sc.read_h5ad("../../data/processed/hsc_progenitors.h5ad")
ad

ad.obs.head().T

print(f"Number of donors: {ad.obs.donor.nunique()}")
print(f"Number of annotated cell types: {ad.obs.celltype_annotation.nunique()}")

ad.obs.groupby("sex").donor.nunique()

ad.obs.celltype_annotation.value_counts()