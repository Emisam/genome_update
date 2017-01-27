import pandas as pd
import compare_isolates as ci

class isolate_finder:

	def __init__(self, assembly_path):
		
		self.frame = self.load_assemblyinfo(assembly_path)
		self.labels = self.find_labels()
		self.compare = ci.compare_isolates()


	def load_assemblyinfo(self,url):
		genbankout = pd.read_table(url, sep='\t', header=1, index_col=0)
		return genbankout

	def find_labels(self):
		indices = {}
		for index, name in enumerate(self.frame.columns.values):
			indices[name] = index
		return indices


	def select_genus(self, target, species_id = None, tax_id = None):
		indices = []
		unique = []
		for i in range(len(self.frame.index)):
			genus = self.frame.iat[i, self.labels['organism_name']].split(' ')
			if target in genus:
				isolate = self.select_isolate(genus[1], i)
				if species_id is not None and species_id != str(self.frame.iat[i, self.labels['species_taxid']]):
					continue
				if tax_id is not None and tax_id != str(self.frame.iat[i, self.labels['taxid']]):
					print('hey from tax')
					continue 
				if isolate not in unique:
					indices.append(i)
					unique.append(isolate)
				else:
					oldIsolate = unique.index(isolate)
					oldIsolateIndex = self.frame.iloc[indices[oldIsolate]] 
					selectedIndex = self.compare.compare_isolates(oldIsolateIndex, self.frame.iloc[i])
					if not selectedIndex.empty:
						newindex = self.frame.index.get_loc(selectedIndex.name)
						indices[oldIsolate] = newindex
						unique[oldIsolate] = self.select_isolate(genus[1], newindex)
		return self.return_isolates(unique, indices)

	def return_isolates(self, names ,indices):
		returnList = []
		for i, j in enumerate(indices):
			tempList = names[i]
			tempList.append(self.frame.iloc[j])
			returnList.append(tempList)
		return returnList

	def select_isolate(self, species, index):
		isolate_name = self.get_isolate_name(index)
		isolate = [species, isolate_name]
		return isolate

	def get_isolate_name(self, index):
		name = self.frame.iat[index, self.labels['infraspecific_name']]
		if pd.isnull(name):
			name = self.frame.iat[index, self.labels['isolate']]
			if pd.isnull(name):
				genus = self.frame.iat[index, self.labels['organism_name']].split(' ')
				if len(genus) > 2:
					name = ' '.join(genus[2:])
				else:
					name = self.frame.iat[index, self.labels['asm_name']]
		else:
			name = name.replace('strain=','')
		return name

