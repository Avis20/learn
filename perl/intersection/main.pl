#!/usr/bin/env perl

my %service_system_map = (
    'qrmenu'          => 'qrmenu',
    'audio_playlists' => 'fm_core',
);

my $services1 = [
  "video",
  "announce",
  "contract_monitoring",
  "audio_playlists_public",
  "audio_playlists_rightholder",
  "audio_playlists_user",
  "smart_playlists",
  "audio_playlists"
];

my $services2 = ['qrmenu'];
my $services3 = ['qrmenu', "smart_playlists", "audio_playlists"];

foreach my $service ( @{$services1 || []} ) {
    if ( %service_system_map{$service} ) {}
};


exit;

