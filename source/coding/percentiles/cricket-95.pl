#!/usr/bin/perl -Tw
###############################################################################
#
#    Cricket 95:  A cricket collection agent that reports the 95th percentile
#                 of an RRD dataset.
#    Copyright (C) 2003 Russell Heilling <russell@ccie.org.uk>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
##############################################################################

use strict;
use RRDs;
use Time::ParseDate;

my @in = ();
my @out = ();
my ($in95Index, $out95Index, @oIn, @oOut);

# usage: cricket-95.pl rrdfile
my ($rrd, $data, $err, $line);
$ARGV[0] =~ ?^(.*)$?;
$rrd = $1;
$data = (RRDs::fetch($rrd, 'AVERAGE', '-s', parsedate('last month')))[3];
$err = RRDs::error;
die "Error fetching data from $rrd: $err\n" if $err;

foreach $line (@$data) {
    if (defined ($$line[0])) {
	push @in, int($$line[0]);
    }
    if (defined ($$line[1])) {
	push @out, int($$line[1]);
    }
}

$in95Index = int(scalar(@in)*0.05)+1;
$out95Index = int(scalar(@out)*0.05)+1;

if (defined($in[$in95Index]) && defined ($out[$out95Index])) {
  @oIn  = sort {$b<=>$a} @in;
  @oOut = sort {$b<=>$a} @out; 

  print "Inbound (samples/peak/95pc index/95pc): ", scalar(@in), "/$oIn[0]/";
  print "$in95Index/$oIn[$in95Index]\n";

  print "Outbound(samples/peak/95pc index/95pc): ", scalar(@out), "/$oOut[0]/";
  print "$out95Index/$oOut[$out95Index]\n";


  print "95th Percentile:\n";

  if ($oIn[$in95Index]>$oOut[$out95Index]){
    print "$oIn[$in95Index]\n";
  } else {
   print "$oOut[$out95Index]\n";
  }
} else {
  print "Not enough readings\n\n95th Percentile:\nU\n";
}