#!/bin/bash

vcf=$1
dir=$(dirname ${vcf})
outbase=$(basename $(basename ${vcf} ".gz") ".vcf")

for i in `tabix -l ${vcf}`
do
    tabix -h ${vcf} ${i} > ${dir}/${outbase}.${i}.vcf && \
        bgzip ${dir}/${outbase}.${i}.vcf && \
        tabix ${dir}/${outbase}.${i}.vcf.gz
done
