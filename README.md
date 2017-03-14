# genome_update

genome_update is a package that downloads genomes from NCBI and saves information about them in a yaml file.
It can also use a local yaml file to update and download new genomes.

Sequence statistics is also calculated for each genome and added to the yaml file.

## Getting Started

These instructions will provide information how to install and use the software.

### Prerequisites

Python 3.5
Pandas
PyYaml


### How to install

To install Genome_update you can either download source code directly from github and build it your self, an easier alternative is to use pip.

Installing by pip:

```
pip install genome_update
```
Pip will also install all prerequisities. It is also recommended to update all prerequisities.

Installing genome_update and upgrading prerequisities: 

```
pip install genome_update --upgrade
```

### Usage

Download all genomes from a specific genus:
```
genome_update -g <Genus>
```

Download all genomes from a specific genus, but much faster:
```
genome_update -g <Genus> -p <threads>
```

Download all genomes from a specific genus, but much faster, to a specific directory (default is /genomes):
```
genome_update -g <Genus> -p <threads> -o <directory>
```

Download all genomes from a specific species:
```
genome_update -g <Genus> -s <species_taxid>
```

To update a local yaml file:
```
genome_update -u -i <yamlfile>
```

To download missing genomes from a local yaml file:
```
genome_update -d -i <yamlfile>
```

To download genomes from another domain than bacteria:
```
genome_update -domain <domain> -g <Genus> 
```



## Authors

* **Emil Samuelsson** - *Initial work* - [Emisam](https://github.com/Emisam)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Would like to thank kblin for his amazing work with the ncbi_genome_download which provided lots of inspiration when writing genome_update.