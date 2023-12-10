#check if gdown is installed
if ! command -v gdown &> /dev/null
then
    pip install gdown
fi

ANNOTATIONS_URL="https://drive.google.com/drive/folders/1E0B4tQdwnqCmQXvqHAaGAXvqu1-I926d"

# download datasets
gdown $ANNOTATIONS_URL -O data/HuPR --folder
# mv data/HuPR/annotations/hrnet_annot_test.json data/HuPR/hrnet_annot_test.json
# mv data/HuPR/annotations/hrnet_annot_train.json data/HuPR/hrnet_annot_train.json
# mv data/HuPR/annotations/hrnet_annot_val.json data/HuPR/hrnet_annot_val.json

# let it like this for now
# use for loop next time
gdown "https://drive.google.com/uc?id=1BuXBbBJ4DsZ7l5f2Y368GDT87M57Zt0F" -O data/HuPR/

# unzip all zip file in HuPR
7z x data/HuPR/*.zip -odata/HuPR/
rm -rf data/HuPR/*.zip