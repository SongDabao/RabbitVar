import argparse

def detectorParam(parser):
  #parser.add_argument('--help', '-H', help = "Print this help page")
  parser.add_argument('--pileup', '-p', help = "Do pileup regardless of the frequency")
  parser.add_argument('--Chr_name', '-C', help = "Indicate the chromosome names are just numbers, such as 1, 2, not chr1, chr2 (deprecated)")
  parser.add_argument('--debug', '-D', help = "Debug mode.  Will print some error messages and append full genotype at the end.")
  parser.add_argument('--dedup', '-t', help = "Indicate to remove duplicated reads.  Only one pair with same start positions will be kept")
  parser.add_argument('--3-prime', '-3', help = "Indicate to move indels to 3-prime if alternative alignment can be achieved.")
  parser.add_argument('--calcu_Ns', '-K', help = "Include Ns in the total depth calculation")
  parser.add_argument('--uni', '-u', help = "Indicate unique mode, which when mate pairs overlap, the overlapping part will be counted only once using forward read only.")
  parser.add_argument('--UN', help = "Indicate unique mode, which when mate pairs overlap, the overlapping part will be counted only once using first read only.")
  parser.add_argument('--chimeric', help = "Indicate to turn off chimeric reads filtering.")
  parser.add_argument('--deldupvar', help = "Turn on deleting of duplicate variants. Variants in this mode are considered and outputted only if start position of variant is inside the region interest.")
  parser.add_argument('--verbose', '-y', help = "")
  parser.add_argument('--Filter', '-F', help = "The hexical to filter reads using samtools. Default: 0x504 (filter 2nd alignments, unmapped reads and duplicates).  Use -F 0 to turn it off.", type=str, required = False)
  parser.add_argument('--zero_based', '-z', help = "Indicate whether coordinates are zero-based, as IGV uses.  Default: 1 for BED file or amplicon BED  file.Use 0 to turn it off. When using the -R option, it's set to 0")
  parser.add_argument('--local_realig', '-k', help = "Indicate whether to perform local realignment.  Default: 1.  Set to 0 to disable it.  For Ion or PacBio, 0 is recommended.", type=int, required = False)
  parser.add_argument('--amplicon', '-a', help = "Indicate it's amplicon based calling. Reads that don't map to the amplicon will be skipped. A read pair is considered belonging to the amplicon if the edges are less than int bp to the amplicon, and overlap fraction is at least float.  Default: 10:0.95", type=str, required = False)
  parser.add_argument('--column', '-c', help = "The column for chromosome", type=int, required = False)
  parser.add_argument('--Genome_fasta', '-G', help = "The reference fasta. Should be indexed (.fai).", type=str, required = True)
  parser.add_argument('--Region', '-R', help = "The region of interest. In the format of chr:start-end. If end is omitted, then a single position.  No BED is needed.", type=str, required = False)
  parser.add_argument("--delemiter", '-d', help = "The delimiter for split region_info, default to tab", type=str, required = False)
  parser.add_argument("--regular_expression", '-n', help = "The regular expression to extract sample name from BAM filenames. Default to: /([^\/\._]+?)_[^\/]*.bam/", required = False)
  parser.add_argument("--Name", '-N', help = "The sample name to be used directly.  Will overwrite -n option", required = False)
  parser.add_argument('--in_bam', '-b', help = "The indexed BAM file", type=str, required = True)
  parser.add_argument('--region_start', '-S', help = "The column for region start, e.g. gene start", type=int, required = False)
  parser.add_argument("--region_end", '-E', help = "The column for region end, e.g. gene end", required = False)
  parser.add_argument('--seg_start', '-s', help = "The column for segment starts in the region, e.g. exon starts", type=int, required = False)
  parser.add_argument('--seg_end', '-e', help = "The column for segment ends in the region, e.g. exon ends", type=int, required = False)
  parser.add_argument('--gene_name', '-g', help = "The column for gene name, or segment annotation", type=int, required = False)
  parser.add_argument('--numcl_extend', '-x', help = "The number of nucleotide to extend for each segment, default: 0", type=int, required = False)
  parser.add_argument('--min', '-B', help = "The minimum # of reads to determine strand bias, default 2", type=int, required = False)
  parser.add_argument('--Quality', '-Q', help = "If set, reads with mapping quality less than INT will be filtered and ignored", type=int, required = False)
  parser.add_argument('--phred_score', '-q', help = "The phred score for a base to be considered a good call.  Default: 25 (for Illumina) For PGM, set it to ~15, as PGM tends to under estimate base quality.", type=float, required = False)
  parser.add_argument('--mismatch', '-m', help = "If set, reads with mismatches more than INT will be filtered and ignored.  Gaps are not counted as  mismatches. Valid only for bowtie2/TopHat or BWA aln followed by sampe.  BWA mem is calculated as NM - Indels.  Default: 8, or reads with more than 8 mismatches will not be used.", type=int, required = False)
  parser.add_argument('--trim', '-T', help = "Trim bases after [INT] bases in the reads", type=int, required = False)
  parser.add_argument('--extension', '-X', help = "Extension of bp to look for mismatches after insersion or deletion.  Default to 2 bp, or only calls when they're within 2 bp.", type=int, required = False)
  parser.add_argument('--Position', '-P', help = "The read position filter.  If the mean variants position is less that specified, it's considered false positive.  Default: 5", type=int, required = False)
  parser.add_argument('--Indel_size', '-I', help = "The indel size.  Default: 50bp", type=int, required = False)
  parser.add_argument('--th', help = "Threads count.", type=int, required = False)
  parser.add_argument('--fisher', help = "Experimental feature: fisher test")
  parser.add_argument('--STD', '-A', help = "The number of STD. A pair will be considered for DEL if INSERT > INSERT_SIZE + INSERT_STD_AMT * INSERT_STD.  Default: 4", type=int, required = False)
  parser.add_argument('--minlen_sv', '-L', help = "The minimum structural variant length to be presented using <DEL> <DUP> <INV> <INS>, etc. Default: 1000. Any indel, complex variants less than this will be spelled out with exact nucleotides.", type=int, required = False)
  parser.add_argument('--ref-extension', '-Y', help = "Extension of bp of reference to build lookup table. Default to 1200 bp. Increase the number will slowdown the program. The main purpose is to call large indels with 1000 bit that can be missed by discordant mate pairs.", type=int, required = False)
  parser.add_argument('--minimum_reads', '-r', help = "The minimum # of variant reads, default 2", type=int, required = False)
  parser.add_argument('--Qratio', '-o', help = "The Qratio of (good_quality_reads)/(bad_quality_reads+0.5).  The quality is defined by -q option.  Default: 1.5", type=float, required = False)
  parser.add_argument('--MapQ', '-O', help = "The reads should have at least mean MapQ to be considered a valid variant.   Default: no filtering", type=float, required = False)
  parser.add_argument('--freq', '-V', help = "The lowest frequency in the normal sample allowed for a putative somatic mutation.   Defaults to 0.05", type=float, required = False)
  parser.add_argument('--allele_fre', '-f', help = "The threshold for allele frequency, default: 0.01", type=float, required = False)
  parser.add_argument('--downsample', '-Z', help = "For downsampling fraction.  e.g. 0.7 means roughly 70 percnet downsampling.  Default: No downsampling. Use with caution.  The downsampling will be random and non-reproducible.", type=float, required = False)
  parser.add_argument('--VS', help = "How strict to be when reading a SAM or BAM. STRICT	- throw an exception if something looks wrong. LENIENT	- Emit warnings but keep going if possible. SILENT	- Like LENIENT, only don't emit warning messages.  Default: LENIENT", type=str, required = False)
  parser.add_argument('--adaptor', help = "Filter adaptor sequences so that they aren't used in realignment. Multiple adaptors can be supplied by setting them with comma, like: --adaptor ACGTTGCTC,ACGGGGTCTC,ACGCGGCTAG .", type=str, required = False)
  parser.add_argument('--crispr', '-J', help = "The genomic position that CRISPR/Cas9 suppose to cut, typically 3bp from the PAM NGG site and  within the guide.  For CRISPR mode only.  It will adjust the variants (mostly In-Del) start and end sites to as close to this location as possible,if there are alternatives. The option should only be used for CRISPR mode.", type=int, required = False)
  parser.add_argument('--CRISPR_fbp', '-j', help = "In CRISPR mode, the minimum amount in bp that a read needs to overlap with cutting site.  If a read does not meet the criteria, it will not be used for variant calling, since it is likely just a partially amplified PCR.  Default: not set, or no filtering", type=int, required = False)
  parser.add_argument('--mfreq', help = "The variant frequency threshold to determine variant as good in case of monomer MSI. Default: 0.25", type=float, required = False)
  parser.add_argument('--nmfreq', help = "The variant frequency threshold to determine variant as good in case of non-monomer MSI. Default: 0.1", type=float, required = False)
  parser.add_argument('--out', help = "The out put file path. Default: ./out.txt", type=str, required = True, default = "./out.txt")
  parser.add_argument('--bed', '-i', help = "The region file to be processed", type=str, required = False)
  parser.add_argument('--version', help = "Print FastVC version information")
  parser.add_argument('--auto_resize', help = "Auto resize the bed region size for better performance")

def filterParm(parser):
  parser.add_argument()

def rabbitvarParam():
  pass

if __name__ == "__main__":
  import sys
  parser = argparse.ArgumentParser(description = "rabbitvar")
  rabbitvar_parser = parser.add_argument_group("rabbitvar_parser")
  detectorParam(rabbitvar_parser)
  args = parser.parse_args()
  print('--------------------')
  for x in rabbitvar_parser._group_actions:
    print(x.dest, getattr(args, x.dest, None))
    #print(x.dest, x.metavar)
  print('--------------------')
  arg_groups = dict()
  #for group in parser._action_groups:
  #  group_dict={a.dest:getattr(args,a.dest,None) for a in group._group_actions}
  #  arg_groups[group.title]=argparse.Namespace(**group_dict)
  #print(arg_groups)
  #args = parser.parse_args() 
  print(sys.argv[1:])
  for k, v in vars(args).items():
    if v is not None:
      print(k, v)
