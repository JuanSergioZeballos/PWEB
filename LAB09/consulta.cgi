#!/usr/bin/perl
use strict;
use warnings;
use CGI;

my $q = CGI->new;
my $nombre = $q->param('nombre');
my $periodo = $q ->param('periodo');
my $departamento = $q->param('departamento');
my $denominacion = $q->param('denominacion');

my $doc_csv = 'Programas de Universidades.csv';
my $csv = Text::CSV->new({binary=>1}) or die "No se puede usar CSV: " . Text::CSV->error_diag();
open my $fh, "<", $doc_csv or die "No se pudo abrir el archivo CSV: $!";

print $q->header("text/html");

