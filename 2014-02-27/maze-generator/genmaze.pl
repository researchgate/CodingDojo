#!/usr/bin/perl

use strict;
use warnings;

use Time::HiRes qw( usleep );
use POSIX;
use Data::Dumper;

my @maze = map {[(undef)x32]} 1..32;
my @path = ();

sub push_path {
   my $px = shift;
   my $py = shift;

   die "px=$px out of bounds" unless $px >= 0 && $px < 32;
   die "py=$py out of bounds" unless $py >= 0 && $py < 32;

   print STDERR "adding path element [$px, $py]\n";
   push @path, [$px, $py];
   $maze[$px][$py] = 1;
}

sub get_directions {
   my $fx = shift;
   my $fy = shift;

   return grep {$_->[0] >= 0 && $_->[0] < 32 && $_->[1] >= 0 && $_->[1] < 32} (

      #       [$fx-1, $fy-1],
      [$fx-1, $fy],

      #       [$fx-1, $fy+1],
      [$fx, $fy-1],

      #       [$fx, $fy],
      [$fx, $fy+1],

      #       [$fx+1, $fy-1],
      [$fx+1, $fy],

      #       [$fx+1, $fy+1],
     );
}

sub get_neighbors {
   my $fx = shift;
   my $fy = shift;

   return grep {$_->[0] >= 0 && $_->[0] < 32 && $_->[1] >= 0 && $_->[1] < 32} (
      [$fx-1, $fy-1],
      [$fx-1, $fy],
      [$fx-1, $fy+1],
      [$fx, $fy-1],

      #       [$fx, $fy],
      [$fx, $fy+1],
      [$fx+1, $fy-1],
      [$fx+1, $fy],
      [$fx+1, $fy+1],
     );
}

sub get_unmarked {
   return grep {!$maze[$_->[0]][$_->[1]]} @_;
}

sub get_marked {
   return grep {$maze[$_->[0]][$_->[1]]} @_;
}

sub print_maze {
   my $buf = "";

   for (1..30) {
      $buf .= "\n";
   }

   my $lineno = 0;
   foreach my $row (@maze) {
      $buf .= sprintf "%2d  ", $lineno;
      foreach my $field (@$row) {
         if ($field) {
            $buf .= ".";
         }
         else {
            $buf .= "#";
         }
      }
      $buf .= "\n";
      $lineno++;
   }

   print STDERR $buf;
}

push_path(0,0);

while (@path) {
   #usleep(9*1000);
   print_maze();

   my $p = $path[$#path];
   my $px = $p->[0];
   my $py = $p->[1];

   my %Np = map {($_->[0]).",".($_->[1]) => 1} get_directions($px, $py);

   my @D = get_unmarked(get_directions($px, $py));
   my @candidates = grep {1 == int(
         grep {!$Np{($_->[0]).",".($_->[1])}} get_marked(get_neighbors($_->[0], $_->[1]))
        )} @D;

   if (@candidates) {
      my $i = floor(rand(int(@candidates)));
      push_path($candidates[$i][0], $candidates[$i][1]);
   }
   else {
      print STDERR "dont know what to do on [$px;$py]\n";
      pop @path;
   }
}

foreach my $row (@maze) {
   foreach my $field (@$row) {
      if ($field) {
         print " ";
      }
      else {
         print "X";
      }
   }
   print "\n";
}
