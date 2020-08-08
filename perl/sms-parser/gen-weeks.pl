#!/usr/bin/env perl

use uni::perl       qw| :dumper |;

use DateTime;

my $year = 2020;
my @start_week = ('02-15/02-22');

my $end;
if ( $ARGV[0] ) {
    my ( $year, $month, $day ) = split('-', $ARGV[0]);
    $end = DateTime->new( year => $year, month => $month, day => $day );
} else {
    $end = DateTime->now();
}

my ($date) = split('/', $start_week[0]);
my ( $month, $day ) = split('-', $date);

my $start = DateTime->new( year => $year, month => $month, day => $day );

my $count = 1;
while ( $end->epoch > $start->epoch ) {
    my $before = $start->clone->add(days => 1);
    $start->add(days => 7);
    printf("W%d\t%s-%s/%s-%s\n",
        $count++,
        $before->strftime('%d'), $before->strftime('%m'),
        $start->strftime('%d'), $start->strftime('%m'),
    );
    
};

exit;