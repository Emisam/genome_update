import gzip
import sys

#fastaparser
def fasta_parser(fasta):
	with gzip.open(fasta,"rb") as fast:
		file = fast.read()
		file = str(file).split(">")
		genomes = []
		file = file[1:]

		for i in file:
			index = i.find('\\n')
			genome = i[index+2:]
			genomes.append(genome.replace("\n", ""))
		return genomes

def contigs(fasta):
	length = []
	for line in fasta: 
		length.append(len(line))

	return [len(length),int(sum(length)/len(length)), sum(length), N50(length)]



def N50(seqlengths):
	seqlength = sorted(seqlengths)
	sum_seq = 0
	for entry in seqlength:
		sum_seq += entry
		if sum_seq >= sum(seqlength)/2:
			return (entry)


def calculate_statistics(yaml,file):
	Dictonary = yaml.read(file)
	Tags = ["Number_of_Contigs", "Average_contig_length", "Number_of_Bases", "N50"]

	print("Calculating sequence statistics...")
	for species in Dictonary:
		for strain in Dictonary[species]:

			fasta = Dictonary[species][strain]["local_fasta"]
			p_fasta = fasta_parser(fasta)
			stats = contigs(p_fasta)

			for i, j in enumerate(stats):
				Dictonary[species][strain][Tags[i]] = j

	print("Writing yaml file...")
	#write yaml
	yaml.write(file,Dictonary)
	print("Done")

##contigs #Average contig length #bases #N50
#argument
#file = sys.argv[1]
#file = "/home/emisam/Genomes/Brucella.yaml"
#genome_dir = sys.argv[2]
#genome_dir = "/home/emisam/Genomes/"
#Open yaml