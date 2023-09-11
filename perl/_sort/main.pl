
use uni::perl       qw| :dumper |;


my %dict = (
    1 => '10',
    2 => '10',
    3 => '10',
    4 => '10',
    5 => '10',
    10 => '10',
    20 => '10',
    30 => '10',
);

foreach my $k ( sort { $a <=> $b } keys %dict ) {
    print "\t $k : $dict{$k}\n";
};

