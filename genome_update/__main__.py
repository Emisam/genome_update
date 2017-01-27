import argparse
import os
import isolate_finder as iso
import yaml_handler as yh
import dictonary_handler as dh
import downloader as dw
def main():


	SUPPORTED_DOMAINS = ['archaea', 'bacteria', 'fungi', 'invertebrate', 'plant', 'protozoa', 'vertebrate_mammalian', 'vertebrate_other', 'viral']
	parser = argparse.ArgumentParser()

	parser.add_argument('-f', '--folder-output', 
						dest = 'folder',
						default = 'genomes/',
						help = 'The folder which files will be downloaded to')
	parser.add_argument('-o', '--output-file', 
						dest = 'output', 
						default = 'genomes.yaml', 
						help = 'The folder which files will be downloaded to')
	parser.add_argument('-p', '--parallel', 
						dest = 'parallel', 
						default = 1, 
						type = int, 
						metavar = "N", 
						help = 'Use N processes to download files (default = 1)')
	parser.add_argument('-i', '--input-file-path', 
						dest = 'input', 
						default = None, 
						help = 'Local yaml file to update')
	
	parser.add_argument('-domain','--domain', 
						dest = 'domain', 
						choices = SUPPORTED_DOMAINS, 
						default = 'bacteria',
						help = 'The domain to download from')
	parser.add_argument('-g', '--genus', 
						dest = 'genus', 
						help = 'Specify the target genus' )
	parser.add_argument('-s', '--species-taxid', 
						dest = 'species_taxid',
						default = None, 
						help = 'Used to specify a target species_taxid' )
	parser.add_argument('-t', '--taxid', 
						dest = 'taxid', 
						default = None, 
						help = 'Used to specify a target taxid')

	parser.add_argument('-d', '--download', 
						dest = 'download', 
						help = 'Use to only download files for all unique isolates in a yaml file', 
						action = 'store_true')
	parser.add_argument('-u', '--update-yaml', 
						dest = 'update', 
						help = 'Use to only update local yaml file', 
						action = 'store_true')


	args = parser.parse_args()


	NCBI = 'ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/' + args.domain + '/assembly_summary.txt'
	yaml = yh.yaml_handler()

	if not os.path.exists(args.folder):
		os.makedirs(args.folder)

	if args.download and args.update:
		print('Both --download and --update-yaml cannot be supplied')
	elif args.download:
		if args.input != None and os.path.exists(args.input):
			download(yaml, args.input, args.output, args.folder, args.parallel)
		else:
			print('To use --download, specify a correct input with -i')
	elif args.update:
		if args.input != None and args.genus and os.path.exists(args.input):
			print('Checking if input is uptodate with NCBI assembly')
			update_yaml(yaml, NCBI, args.genus, args.species_taxid, args.taxid, args.output, args.input)
		else:
			print('To use --download, specify a correct input with -i')
	elif args.genus:
		update_yaml(yaml, NCBI, args.genus, args.species_taxid, args.taxid, args.output, args.input)
		download(yaml, args.output, args.output, args.folder, args.parallel)
	else:
		print('Input arguments was invalid, try -h for help')
def download(yaml, inputfile, outputfile, directory, parallel):
	dwon = dw.downloader(yaml.read(inputfile))
	job = dwon.get_download_jobs(directory)
	if len(job) != 0:
		newdict = dwon.download_jobs(parallel, job)
		yaml.write(outputfile, newdict)
	else:
		print('Could not find any jobs, check if genus and species-taxid is correctly entered')

def update_yaml(yaml, url, genus, species_taxid, taxid, outputfile, inputfile):
	dl = iso.isolate_finder(url)
	isolates = dl.select_genus(genus, species_taxid, taxid)
	dictonary = dh.dictonary(yaml, outputfile, inputfile)
	dictonary.update_dictonary(isolates, genus)

if __name__ == '__main__':
	main()