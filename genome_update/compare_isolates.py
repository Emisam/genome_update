from datetime import datetime
class compare_isolates:

	def compare_isolates(self, isolate1, isolate2):
		reference = ['Complete genome', 'Chromosome', 'Scaffold', 'Contig']
		label = 'assembly_level'
		assembly1 = isolate1[label]
		assembly2 = isolate2[label]
		if assembly1 == assembly2:
			return self.check_paired(isolate1, isolate2)
		else: #change for dictonatry
			for i in reference:
				if i == assembly1:
					return isolate1
				elif i == assembly2:
					return isolate2
			return []


	def check_paired(self, isolate1, isolate2):
		pac_label = 'paired_asm_comp'
		paired1 = isolate1[pac_label]
		paired2 = isolate2[pac_label]
		if paired1 == paired2:
			return self.check_mostrecent(isolate1, isolate2)
		elif paired1 == 'identical':
			return isolate1
		elif paired2 == 'identical':
			return isolate2
		else:
			return -1

	def check_mostrecent(self, isolate1, isolate2):
		label = 'seq_rel_date'
		timeformat = "%Y/%m/%d"
		date1 = datetime.strptime(isolate1[label], timeformat)
		date2 = datetime.strptime(isolate2[label], timeformat)
		if date1 > date2:
			return isolate1
		elif date2 > date1:
			return isolate2
		else:
			return isolate1