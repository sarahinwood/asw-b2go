#!/usr/bin/env bash

set -eu

run_blastx () {
    local _input_chunk
    local _outdir
    local _bn

    _input_chunk="${1}"
    _bn=$(basename "${_input_chunk}" .fasta)
    _outdir="output/blastx/${_bn/trinity_/}"

    if [[ ! -e "${_outdir}" ]]; then
        mkdir -p "${_outdir}"
    fi

    blastx \
        -query "${_input_chunk}" \
        -task blastx-fast \
        -db "data/blastdb/refseq_protein/refseq_protein" \
        -out "${_outdir}/results.xml" \
        -outfmt 5 \
        -num_threads 40
}

export -f run_blastx

find "output/fasta_chunks/" -name "*.fasta" \
    -exec bash -c 'run_blastx "${0}"' {} \;
