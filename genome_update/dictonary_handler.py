# -*- coding: utf-8 -*-
import compare_isolates as ci
import os.path
import itertools
class dictonary:
	def __init__(self, handler, outputfile, inputfile = None):
		self.output_path = outputfile
		self.input_path = inputfile
		self.handler = handler
		self.compare = ci.compare_isolates()

	def insert(self, dictonary, species, isolate, data):	
		dictonary = dictonary
		list_isolates = list(itertools.chain.from_iterable(dictonary.values()))	
		if isolate not in list_isolates:
			if species in dictonary:
				selected_species = dictonary[species]
				print('Adding new isolate %s to species: %s' % (isolate ,species))
				selected_species[isolate] = data
			else:
				print('Adding new species: %s to yaml file' %species)
				dictonary[species] = {isolate : data}
		else:
			iso_species = ""
			for s in dictonary:
				if isolate in dictonary[s]:
					iso_species = s
					break
			selected_species = dictonary[iso_species]
			selected_isolate = selected_species[isolate]
			new_isolate = self.compare.compare_isolates(selected_isolate, data)
			if len(set(selected_isolate.values()).difference(new_isolate.values())) > 0: 
				print('There is a more complete or newer version of isolate %s in species %s' % (isolate,species))
		return dictonary
	def create_dict(self, isolate):
		newColumns = ['local_fasta', 'local_gbk', 'local_gff']
		dicto = {}
		indeces = isolate.index
		assembly = 'assembly_accession'
		dicto[assembly] = isolate.name
		for i, j in enumerate(isolate):
			dicto[indeces[i]] = str(j)
		for i in newColumns:
			dicto[i] = ""
		return dicto

	def update_dictonary(self, isolates,  genus):
		local = {}
		if (self.input_path != None):
			local = self.handler.read(self.input_path)
		
		for i in isolates:
			dicto = self.create_dict(i[2])
			local = self.insert(local, genus +' '+ i[0], i[1], dicto)
		self.handler.write(self.output_path,local)
