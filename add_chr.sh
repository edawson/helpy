#!/bin/bash

vcf=$1
out=$(dirname $vcf)/$(basename $vcf .vcf.gz).chr.vcf.gz
awk '{if($0 !~ /^#/) print "chr"$0; else print $0}' <(bgzip -d -c -@2 ${vcf}) | bgzip -@2 -c > ${out} && tabix $out
