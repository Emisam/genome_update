# -*- coding: utf-8 -*-
import urllib
import os
from multiprocessing import Pool

class downloader:
	def __init__(self, genome):
		self.genomes = genome
		self.file_labels = ['local_fasta', 'local_gbk', 'local_gff']
		self.file_formats = ['fna.gz', 'gbff.gz', 'gff.gz']
	def get_download_jobs(self, outfolder):
		jobs = []
		for species in self.genomes.keys():
			for strain in self.genomes[species].keys():
				for j, i in enumerate(self.file_labels):
					path = self.genomes[species][strain][i]
					if path == '' or path == None:
						assembly = self.genomes[species][strain]['assembly_accession']
						asm_name = self.genomes[species][strain]['asm_name'].replace(' ','_').replace('/',"_")
						ftp_path = self.genomes[species][strain]['ftp_path']
						ftp_path = '/'.join([ftp_path , ftp_path[ftp_path.find(assembly):]])
						ftp_path = ftp_path +'_'+ 'genomic' +'.'+ self.file_formats[j]
						file_name = os.path.join(outfolder, self.clean_name(strain) + "." + self.file_formats[j])
						jobs.append([ftp_path, file_name, species, strain, i])
		return jobs

	def download(self, job):
		try:
			urllib.request.urlretrieve(job[0], job[1])
			print('Download of %s complete' %job[1])
			return True
		except urllib.error.HTTPError:
			print('Download of %s failed could not find ftp: '%job[0])
			return False
		except:
			print('Unexpected error, skipping thread')
			return False

	def download_jobs(self, parallel, jobs):
		print('Downloading jobs....')
		pool = Pool(processes=parallel)
		pool.map(self.download, jobs)
		print('Download of %i  genomes complete' %int(len(jobs)/3))
		return self.check_files(jobs)

	def check_files(self, jobs):
		for job in jobs:
			if os.path.isfile(job[1]):
				self.genomes[job[2]][job[3]][job[4]] = job[1]
		return self.genomes

	def clean_name(self, string):
		newstring = string.replace('(','_')
		newstring = newstring.replace(')','_')
		newstring = newstring.replace('/','_')
		newstring = newstring.replace(' ','_')
		return newstring