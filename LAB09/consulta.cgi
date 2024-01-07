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
while (my $row = $csv->getline($fh)) {
    my $universidad = $row->[1];
    if (
        grep {
            my $columna = $_;
            $columna =~ /$nombre/i ||
            $columna =~ /$periodo/i ||
            $columna =~ /$departamento/i ||
            $columna =~ /$denominacion/i
        } @$row
    ) {
		print "Universidad: $universidad<br>";
        for my $i (0 .. $#{$row}) {
            print "Columna $i: $row->[$i]<br>";
        }
        print "<hr>";
    }
}
close $fh;
print "No se encontraron coincidencias." unless $q->param;
