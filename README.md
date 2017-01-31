A script that downloads genomes for a selected genus/species/subspecies from NCBI assembly file.
Can also be used to update a local directory with a specified yaml file.  


usage: genome_downloader.py [-h] [-f FOLDER] [-o OUTPUT] [-p N] [-i INPUT] [-domain Bacteria] [-g GENUS] [-s SPECIES_TAXID] [-t TAXID] [-d] [-u]


arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, folder, --output FOLDER 
The folder which files will be downloaded to 

-name NEWNAME, --newname NEWNAME
What the yaml file should be named

-p N, --parallel N
Use N processes to download files (default = 1)
 
-i INPUT, --input-file-path INPUT
Local yaml file to update

-domain, --domain 
{archaea,bacteria,fungi,invertebrate,plant,protozoa,vertebrate_mammalian,vertebrate_other,viral}
The domain to download from

-g GENUS, --genus GENUS
Specify the target genus
  
-s SPECIES_TAXID, --species-taxid SPECIES_TAXID
Used to specify a target species_taxid

-t TAXID, --taxid TAXID
Used to specify a target taxid

-d, --download
Use to only download files for all unique isolates a yaml file

-u, --update-yaml
Use to only update local yaml file


Example: To download all genomes from brucella with 10 processes to the folder Brucella-genomes
genome_update -g Brucella -p 10 -o Brucella-genomes