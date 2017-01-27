A script that downloads genomes for a selected genus/species/subspecies from NCBI assembly file.
Can also be used to update a local directory with a specified yaml file.  


usage: genome_downloader.py [-h] [-f FOLDER] [-o OUTPUT] [-p N] [-i INPUT]
               [-domain {archaea,bacteria,fungi,invertebrate,plant,protozoa,vertebrate_mammalian,vertebrate_other,viral}]
               [-g GENUS] [-s SPECIES_TAXID] [-t TAXID] [-d] [-u]



optional arguments:
  -h, --help            show this help message and exit
  -f FOLDER, --folder-output FOLDER 
                        The folder which files will be downloaded to
  -o OUTPUT, --output-file OUTPUT
                        The folder which files will be downloaded to
  -p N, --parallel N    Use N processes to download files (default = 1)
  -i INPUT, --input-file-path INPUT
                        Local yaml file to update
  -domain {archaea,bacteria,fungi,invertebrate,plant,protozoa,vertebrate_mammalian,vertebrate_other,viral}, 
  --domain {archaea,bacteria,fungi,invertebrate,plant,protozoa,vertebrate_mammalian,vertebrate_other,viral}
                        The domain to download from
  -g GENUS, --genus GENUS
                        Specify the target genus
  -s SPECIES_TAXID, --species-taxid SPECIES_TAXID
                        Used to specify a target species_taxid
  -t TAXID, --taxid TAXID
                        Used to specify a target taxid
  -d, --download        Use to only download files for all unique isolates in
                        a yaml file
  -u, --update-yaml     Use to only update local yaml file
