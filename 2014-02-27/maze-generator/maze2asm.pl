#!/usr/bin/perl

use strict;
use warnings;

my $startaddr = 0x0200;

my %colmap = (
   "X" => "X",
   " " => "A",
);

printf "LDX #\$00\n"; # color of walls
printf "LDA #\$0e\n"; # color of free space
printf "\n";

while (my $line = <>) {
   chomp $line;

   die "wrong length" unless length($line) == 32;
   my @pixels = map {$colmap{$_}} split //, $line;

   for (my $i=0; $i<int(@pixels); $i++) {
      if (defined($pixels[$i])) {
         printf "ST%s \$%04x\n", $pixels[$i], $startaddr+$i;
      }
   }

   $startaddr += 32;
}
