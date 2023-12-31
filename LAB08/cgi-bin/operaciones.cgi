#!usr/bin/perl
use strict;
use CGI;
my $cgi = new CGI;
my $text = $cgi->param('operacion');
if($text=~ m/(.+)*(.+)/){
	$num1=$1;
	$num2=$2;
	$result=$num1*$num2;
	print $cgi->header("text/html");
    print 'El resultado de la division es: '.$result;
}