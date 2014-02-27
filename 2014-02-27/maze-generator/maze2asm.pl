#!/usr/bin/perl

use strict;
use warnings;

my $startaddr = 0x0200;

my %colmap = (
   "X" => 0x00,
   " " => 0x0e,
);

while (my $line = <>) {
   chomp $line;

   die "wrong length" unless length($line) == 32;
   my @pixels = map {$colmap{$_}} split //, $line;

   for (my $i=0; $i<int(@pixels); $i++) {
      if (defined($pixels[$i])) {
         printf "LDA #\$%02x\n", $pixels[$i];
         printf "STA \$%04x\n", $startaddr+$i;
         printf "\n";
         
      }
   }

   $startaddr += 32;
}
