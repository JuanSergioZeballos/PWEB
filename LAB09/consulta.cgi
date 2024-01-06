#!/usr/bin/perl
use strict;
use warnings;
use CGI;

my $q = CGI->new;
my $nombre = $q->param('nombre');
my $periodo = $q ->param('periodo');
my $departamento = $q->param('departamento');
my $denominacion = $q->param('denominacion');

