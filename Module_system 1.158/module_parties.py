from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0
#pf_town = pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small

#sample_party = [(trp_swadian_knight,1,0), (trp_swadian_peasant,10,0), (trp_swadian_crossbowman,1,0), (trp_swadian_man_at_arms, 1, 0), (trp_swadian_footman, 1, 0), (trp_swadian_militia,1,0)]

# NEW TOWNS:
# NORMANDY: Rouen, Caen, Bayeux, Coutances, Evreux, Avranches
# Brittany: Rennes, Nantes,
# Maine: Le Mans
# Anjou: Angers


parties = [
  ("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(17, 52.5),[(trp_player,1,0)]),
  ("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(1,1),[(trp_temp_troop,3,0)]),
#parties before this point are hardwired. Their order should not be changed.

  ("temp_party_2","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
#Used for calculating casulties.
  ("temp_casualties","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_2","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_3","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_wounded","{!}enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_killed", "{!}enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("main_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("encountered_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("player_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("ally_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  ("collective_enemy","{!}collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  #TODO: remove this and move all to collective ally
  ("collective_ally","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
   
  ("total_enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #ganimet hesaplari icin #new:
  ("routed_enemies","{!}routed_enemies",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #new:  

#  ("village_reinforcements","village_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

###############################################################  
  ("freelancer_party_backup","{!}",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),#TU jineng_xiaobing
  
  ("zendar","Zendar",   icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.62,-62.86),[]),
##########tiandishanzei##########
  ("penglaidao","penglaidao",   icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-87.420000,-51.970000),[]),
  ("haichuan","haichuan",   icon_ship|pf_is_static|pf_always_visible|pf_is_ship, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.500000,14.000000),[]),
  
  ("town_1","Sargoth",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.949710,17.537020),[], 170),
  ("town_2","Tihr",     icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.051571,45.386799),[], 120),
  ("town_3","Veluca",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.082989,16.303049),[], 80),
  ("town_4","Suno",     icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.180000,-5.140000),[], 290),
  ("town_5","Jelkala",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40.114639,27.146111),[], 90),
  ("town_6","Praven",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.032110,-5.570555),[], 155),
  ("town_7","Uxkhal",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-0.060000,1.330000),[], 240),

  ("town_8","Reyvadin", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.472702, 32.582150),[], 175),
  ("town_9","Khudan",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62.411221, 8.138440),[], 90),
  ("town_10","Tulga",   icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.890000, -23.660000),[], 310),
  ("town_11","Curaw",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.365623, 31.359570),[], 150),
  ("town_12","Wercheg", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.270010, 34.804740),[], 25),
  ("town_13","Rivacheg",icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.510281, -13.414720),[], 60),
  ("town_14","Halmar",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45.500000, -30.000000),[], 135),

  ("town_15","Yalen",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.421650, 28.670670),[], 45),
  ("town_16","Dhirim",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.795590, 12.189780),[], 0),
  ("town_17","Ichamur",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.794360, -63.624020),[], 90),
  ("town_18","Narra",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.615387, -25.715490),[], 135),

  ("town_19","Shariz", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(109.863701, -49.695801),[], 45),
  ("town_20","Durquba", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.973656, 5.943705),[], 270),
  ("town_21","Ahmerrad", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62.278839, 82.214050),[], 330),
  ("town_22","Bariyye", icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.450000, -35.750000),[], 225),
  ("town_23","Changsha", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-0.421700, 59.284360),[], 225),
  ("town_24","Changsha", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.070000, 51.720000),[], 225),
  ("town_25","Changsha", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.680000, -41.970000),[], 225),
  ("town_26","Changsha", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.490000, -12.720000),[], 225),
  ("town_27","Changsha", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(22.160000, -37.400000),[], 225),
  ("town_28","Changsha", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-118.410000, -43.550000),[], 225),
  ("town_29","Changsha", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.130000, -56.810000),[], 225),
  ("town_30","Changsha", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-87.800000, -78.280000),[], 225),
  ("town_31","Changsha", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.890000, -64.030000),[], 225),
  ("town_32","Changsha", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65.720000, 38.260000),[], 225),
  
#   Aztaq_Castle       
#  Malabadi_Castle
  ("castle_1","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.945360, 54.955311),[],50),
  ("castle_2","Malayurg_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-22.318501, -17.310760),[],75),
  ("castle_3","Bulugha_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.748920, 13.540810),[],100),
  ("castle_4","Radoghir_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.687950, -36.108109),[],180),
  ("castle_5","Tehlrog_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.427544, 52.121090),[],90),
  ("castle_6","Tilbaut_Castle",icon_map_sdgicon_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.423798, 13.122450),[],-0.630068 * (180.0 / 3.1415926)),
  ("castle_7","Sungetche_Castle",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-74.830000, -53.480000),[],45),
  ("castle_8","Jeirbe_Castle",icon_map_sdgicon_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84.759911, 18.949530),[],-1.306401 * (180.0 / 3.1415926)),
  ("castle_9","Jamiche_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-108.715103, -51.538731),[],100),
  ("castle_10","Alburq_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-22.000000, -52.500000),[],110),
  ("castle_11","Curin_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(93.625160, -35.050228),[],75),
  ("castle_12","Chalbek_Castle",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.710000, -43.210000),[],95),
  ("castle_13","Kelredan_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(29.379110, -2.249971),[],115),
  ("castle_14","Maras_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.168671, 39.420570),[],90),
  ("castle_15","Ergellon_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89.197243, 83.721298),[],235),
  ("castle_16","Almerra_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-23.660000, 42.990000),[],45),
  ("castle_17","Distar_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.660000, -4.990000),[],15),
  ("castle_18","Ismirala_Castle",icon_map_sdgicon_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.747231, 5.045403),[],5.235988 * (180.0 / 3.1415926)),
  ("castle_19","Yruma_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(73.539783, 4.573746),[],280),
  ("castle_20","Derchios_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.200560, -36.235031),[],260),
  ("castle_21","Ibdeles_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.921700, 53.984360),[],260),
  ("castle_22","Unuzdaq_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.690000, -33.730000),[],260),
  ("castle_23","Tevarin_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-39.610000,7.780000),[],80),
  ("castle_24","Reindi_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.890000, 2.430000),[],260),
  ("castle_25","Ryibelet_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(38.950000, 74.770000),[],260),
  ("castle_26","Senuzgda_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.842000, 11.878210),[],260),
  ("castle_27","Rindyar_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.410000, -6.600000),[],260),
  ("castle_28","Grunwalder_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.476250, 103.313698),[],260),

  ("castle_29","Nelag_Castle",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(79.699997, -85.400002),[],280),
  ("castle_30","Asugan_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25.414890, -19.550920),[],260),
  ("castle_31","Vyincourd_Castle",icon_map_sdgicon_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.773120, -5.419148),[],4.537856 * (180.0 / 3.1415926)),
  ("castle_32","Knudarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.040000, -47.590000),[],260),
  ("castle_33","Etrosq_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.710000, 87.810000),[],80),
  ("castle_34","Hrus_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.206490, -60.030258),[],260),
  ("castle_35","Haringoth_Castle",icon_map_sdgicon_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(37.476410, -7.282485),[],4.537856 * (180.0 / 3.1415926)),
  ("castle_36","Jelbegi_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.061001, -70.387093),[],260),
  ("castle_37","Dramug_Castle",icon_map_sdgicon_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(66.209602, -17.135300),[],5.711857 * (180.0 / 3.1415926)),
  ("castle_38","Tulbuk_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.706820, -36.351689),[],260),
  ("castle_39","Slezkh_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.876738, -7.424837),[],280),
  ("castle_40","Uhhun_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(95.061287, 69.767738),[],260),

  ("castle_41","Jameyyed_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.216395, -59.482800),[],260),
  ("castle_42","Teramma_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.631760, -7.021946),[],80),
  ("castle_43","Sharwa_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(138.325302, -73.408524),[],260),
  ("castle_44","Durrin_Castle",icon_map_sdgicon_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(69.444267, -7.326901),[],5.789053 * (180.0 / 3.1415926)),
  ("castle_45","Caraf_Castle",icon_map_sdgicon_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.133690, -19.293480),[],4.537856 * (180.0 / 3.1415926)),
  ("castle_46","Weyyah_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.713539, -44.271790),[],260),
  ("castle_47","Samarra_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.174797, -27.017361),[],260),
  ("castle_48","Bardaq_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(45.564610, 41.061272),[],260),
  ## fysg new castles
  # Swadia
  ("castle_49","Deglan_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.554812, 43.302151),[],100),
  ("castle_50","Tredian_Castle",icon_map_sdgicon_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.413029, -36.740700),[],1.919862 * (180.0 / 3.1415926)),
  ("castle_51","Grainwad_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.502541, 36.737179),[],75),
  ("castle_52","Ryis_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.950000, -10.700000),[],95),
  ("castle_53","Stamar_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(20.020010, -43.747060),[],115),
  # Vaegirs
  # ("castle_54","Doru_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(81.523013, 4.235621),[],90),
  # ("castle_55","Gastya_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,( 73.092178, -32.506290),[],235),
  # Khergit
  ("castle_56","Sebula_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.185741, 21.865070),[],260),
  # Nords
  ("castle_57","Turegor_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(91.065666, -28.792690),[],260),
  ("castle_58","Rayeck_Castle",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65.500000, -79.500000),[],260),
  # Rhodoks
  ("castle_59","Reland_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.442320, 77.643471),[],280),
  # ("castle_60","Falsevor_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.715231, 54.918591),[],260),
  ("castle_61","Reichsin_Castle",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40.675880, 76.856659),[],80),
  # Sarranid
  ("castle_62","Ghulassen_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.704369, 67.846184),[],260),
  # ("castle_63","Muhnir_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.421650, 28.670670),[],260),
  ("castle_64","Biliya_Castle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(86.437263, 126.275299),[],260),
## fysg
 

#     Rinimad      
#              Rietal Derchios Gerdus
# Tuavus   Pamir   vezona 
  ("castle_65","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43.330000, -19.780000),[],50),
  ("castle_66","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.460000, -11.090000),[],50),
  ("castle_67","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.030000, -7.510000),[],50),
  ("castle_68","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.860000, 12.170000),[],50),
  ("castle_69","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.530000, 58.410000),[],50),
  ("castle_70","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.390000, -19.700000),[],50),
  ("castle_71","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.240000, -14.370000),[],50),
  ("castle_72","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.855230, -27.670600),[],50),
  ("castle_73","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.850000, -25.770000),[],50),
  ("castle_74","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.540000, -24.570000),[],50),
  ("castle_75","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-116.960000, -33.820000),[],50),
  ("castle_76","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.760000, -49.920000),[],50),
  ("castle_77","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.480000, 5.660000),[],50),
  ("castle_78","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.720000, -30.260000),[],50),
  ("castle_79","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.180000, 13.870000),[],50),
  ("castle_80","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-36.100000, 24.380000),[],50),
  ("castle_81","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.970000, 31.640000),[],50),
  ("castle_82","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54.100000, 29.490000),[],50),
  ("castle_83","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-36.160000, 33.020000),[],50),
  ("castle_84","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.570000, 34.270000),[],50),
  ("castle_85","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-52.970000, 26.190000),[],50),
  ("castle_86","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(36.990000, 98.710000),[],50),
  ("castle_87","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.440000, -10.870000),[],50),
  ("castle_88","Culmarr_Castle",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.510000, -14.390000),[],50),
  
  ("village_1", "Yaragar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.986810, -0.584838),[], 100),
  ("village_2", "Burglen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.976890, -18.261520),[], 110),
  ("village_3", "Azgad",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.138769, 44.148289),[], 120),
  ("village_4", "Nomar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.389111, 66.443443),[], 130),
  ("village_5", "Kulum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(94.794197, 101.907799),[], 170),
  ("village_6", "Emirin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.930969, -59.449139 ),[], 100),
  ("village_7", "Amere",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.940110, 33.765041),[], 110),
  ("village_8", "Haen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(98.383797, -33.118980),[], 120),
  ("village_9", "Buvran",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.985603, 45.259140),[], 130),
  ("village_10","Mechin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(141.065399, -84.477600),[], 170),

  ("village_11","Dusturil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(20.337659, 1.040500),[], 100),
  ("village_12","Emer",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-55.757660, 62.421169),[], 110),
  ("village_13","Nemeja",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9.082262, 33.398029),[], 120),
  ("village_14","Sumbuja",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.784308, 7.893908),[], 130),
  ("village_15","Ryibelet",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.483315, -53.425011),[], 170),
  ("village_16","Shapeshte",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.015231, 42.018591),[], 170),
  ("village_17","Mazen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.270309, 15.260970),[], 35),
  ("village_18","Ulburban",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.790979, -57.637301),[], 170),
  ("village_19","Hanun",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.790000, -41.100000),[], 170),
  ("village_20","Uslum",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.845291, 8.783070),[], 170),

  ("village_21","Bazeck",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-22.187820, -10.127110),[], 100),
  ("village_22","Shulus",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-86.844239, -68.593993),[], 110),
  ("village_23","Ilvia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.885890, 26.392851),[], 120),
  ("village_24","Ruldi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34.893070, 1.737903),[], 130),
  ("village_25","Dashbigha",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.066750, 42.332581),[], 170),
  ("village_26","Pagundur",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.617340, 55.433022),[], 170),
  ("village_27","Glunmar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.575241, 47.774090),[], 170),
  ("village_28","Tash_Kulun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.932190, 2.823776),[], 170),
  ("village_29","Buillin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63.599998, 33.900002),[], 170),

  ("village_30","Ruvar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(79.264226, -8.918940),[], 170),
  ("village_31","Ambean",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-23.418579, 66.885567),[], 100),
  ("village_32","Tosdhar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.294460, 1.491630),[], 110),
  ("village_33","Ruluns",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-52.873508, 24.026560),[], 120),
  ("village_34","Ehlerdah",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(37.534161, 39.655551),[], 130),
  ("village_35","Fearichen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.039280, 7.320295),[], 170),
  ("village_36","Jayek",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.593534, 11.849400),[], 170),
  ("village_37","Ada_Kulun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.140000, -34.840000),[], 170),
  ("village_38","Ibiran",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(93.271950, 82.553520),[], 170),
  ("village_39","Reveran",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(50.639740, 122.065598),[], 170),
  ("village_40","Saren",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.144909, 90.064117),[], 170),

  ("village_41","Dugan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-22.160000, -33.170000),[], 100),
  ("village_42","Dirigh_Aban",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(24.025009, -31.059731),[], 110),
  ("village_43","Zagush",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.934879, 23.547850),[], 120),
  ("village_44","Peshmi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.061897, 27.671000),[], 130),
  ("village_45","Bulugur",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(57.537104, 40.296049),[], 170),
  ("village_46","Fedner",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.296371, 46.098709),[], 170),
  ("village_47","Epeshe",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.090000, 59.290000),[], 170),
  ("village_48","Veidar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84.934807, 13.458940),[], 170),
  ("village_49","Tismirr",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.250912, 32.999592),[], 10),
  ("village_50","Karindi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.854389, 8.782099),[], 170),

  ("village_51","Jelbegi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.040000, -42.100000),[], 100),
  ("village_52","Amashke",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(69.808823, 44.289391),[], 110),
  ("village_53","Balanli",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28.361259, 26.659349),[], 120),
  ("village_54","Chide",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.948879, 31.965570),[], 130),
  ("village_55","Tadsamesh",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.225268, 5.851194),[], 170),
  ("village_56","Fenada",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.297981, 88.603867),[], 170),
  ("village_57","Ushkuru",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.093540, -7.868196),[], 170),
  ("village_58","Vezin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21.806200, -58.054710),[], 170),
  ("village_59","Dumar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.502819, 38.746769),[], 170),
  ("village_60","Tahlberl",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(50.144810, -18.946859),[], 170),

  ("village_61","Aldelen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(72.124763, -39.569580),[], 100),
  ("village_62","Rebache",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(20.773760, 17.727150),[], 100),
  ("village_63","Rduna",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(42.780602, -13.021270),[], 100),
  ("village_64","Serindiar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(42.959900, 5.698090),[], 100),
  ("village_65","Iyindah",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.416300, 16.517820),[], 100),
  ("village_66","Fisdnar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.474560, -34.888248),[], 100),
  ("village_67","Tebandra",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.420514, -20.619431),[], 100),
  ("village_68","Ibdeles",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(77.526031, 39.732609),[], 100),
  ("village_69","Kwynn",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(47.535982, -4.107350),[], 100),
  ("village_70","Dirigsene",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.975901, 90.949837),[], 100),

  ("village_71","Tshibtin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.096481, 21.484810),[], 20),
  ("village_72","Elberl",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.466293, 77.893440),[], 60),
  ("village_73","Chaeza",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18.130000, -15.270000),[], 55),
  ("village_74","Ayyike",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.432088, 54.311119),[], 15),
  ("village_75","Bhulaban",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.987640, 18.408760),[], 10),
  ("village_76","Kedelke",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.338350, 4.967332),[], 35),
  ("village_77","Rizi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.165110, -19.154560),[], 160),
  ("village_78","Sarimish",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(29.667830, -13.066210),[], 180),
  ("village_79","Istiniar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.438248, 73.302437),[], 0),
  ("village_80","Vayejeg",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(96.394279, 94.538628),[], 40),

  ("village_81","Odasan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.883091, 111.632004),[], 20),
  ("village_82","Yalibe",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-66.270988, 47.423439),[], 60),
  ("village_83","Gisim",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.650000, -26.020000),[], 55),
  ("village_84","Chelez",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.114109, 86.781082),[], 15),
  ("village_85","Ismirala",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.587271, 32.444191),[], 10),
  ("village_86","Slezkh",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(66.872402, -29.750649),[], 35),
  ("village_87","Udiniad",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.332631, -55.004006),[], 160),
  ("village_88","Tulbuk",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.984100, -19.272640),[], 180),
  ("village_89","Uhhun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.973900, -2.226740),[], 0),
  ("village_90","Jamiche",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(77.410102, -25.783341),[], 40),

  ("village_91","Ayn Assuadi",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(73.799998, -16.359999),[], 20),
  ("village_92","Dhibbain",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.885890, 28.392851),[], 60),
  ("village_93","Qalyut",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-20.000000, 98.800003),[], 55),
  ("village_94","Mazigh",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.570002, 8.380000),[], 15),
  ("village_95","Tamnuh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.070000, -11.520000),[], 10),
  ("village_96","Habba",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(112.000000, -66.000000),[], 35),
  ("village_97","Sekhtem",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(93.600003, -26.070000),[], 160),
  ("village_98","Mawiti",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.700001, -80.199997),[], 180),
  ("village_99","Fishara",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(72.699998, 10.060000),[], 0),
  ("village_100","Iqbayl",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28.000000, -52.500000),[], 40),

  ("village_101","Uzgha",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.000000, 43.500000),[], 20),
  ("village_102","Shibal Zumr",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.200000, -72.000000),[], 60),
  ("village_103","Mijayet",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.300001, -65.450002),[], 55),
  ("village_104","Tazjunat",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(108.000000, -36.500000),[], 15),
  ("village_105","Aab",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(57.000000, -49.500000),[], 10),
  ("village_106","Hawaha",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.610003, -4.920000),[], 35),
  ("village_107","Unriya",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.5558, 14.631000),[], 160),
  ("village_108","Mit Nun",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(126.800003, -73.300003),[], 180),
  ("village_109","Tilimsal",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(50.000000, 92.500000),[], 0),
  ("village_110","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.900000, 114.500000),[], 40),
  ###TU 13.1.13
  ("village_111","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.220000, -67.960000),[], 40),
  ("village_112","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.180000, -48.140000),[], 40),
  ("village_113","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.790000, -29.610000),[], 40),
  ("village_114","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.360000, -15.030000),[], 40),
  ("village_115","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-11.710000, -21.450000),[], 40),
  ("village_116","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.970000, -14.680000),[], 40),
  ("village_117","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.000000, -1.000000),[], 40),
  ("village_118","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-67.800000, -29.860000),[], 40),
  ("village_119","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.570000, -5.660000),[], 40),
  ("village_120","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-52.490000, -29.200000),[], 40),
  ("village_121","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.134000, -7.841000),[], 40),
  ("village_122","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.134000, -2.041000),[], 40),
  ("village_123","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.754000, -0.491000),[], 40),
  ("village_124","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.264000, 0.551000),[], 40),
  ("village_125","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(20.604000, -4.901000),[], 40),
  ("village_126","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.884000, 5.231000),[], 40),
  ("village_127","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.714000, 10.731000),[], 40),
  ("village_128","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.054000, 9.811000),[], 40),
  ("village_129","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.480000, -30.470000),[], 40),
  ("village_130","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.350000, -27.620000),[], 40),
  ("village_131","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.180000, 55.070000),[], 40),
  ("village_132","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.440000, -24.960000),[], 40),
  ("village_133","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.270000, -16.540000),[], 40),
  ("village_134","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.290000, -13.730000),[], 40),
  ("village_135","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28.800000, -20.430000),[], 40),
  ("village_136","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.080000, -2.690000),[], 40),
  ("village_137","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.490000, 86.360000),[], 40),
  ("village_138","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-22.910000, -41.690000),[], 40),
  ("village_139","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.730000, -25.370000),[], 40),
  ("village_140","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.330000, -23.660000),[], 40),
  ("village_141","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-105.740000, -45.740000),[], 40),
  ("village_142","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-106.390000, -40.060000),[], 40),
  ("village_143","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.850000, -24.110000),[], 40),
  ("village_144","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(59.300000, -33.030000),[], 40),
  ("village_145","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(47.820000, -27.280000),[], 40),
  ("village_146","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-111.760000, -64.290000),[], 40),
  ("village_147","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.320000, 36.310000),[], 40),
  ("village_148","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.250000, 37.010000),[], 40),
  ("village_149","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.060000,35.100000),[], 40),
  ("village_150","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.150000, 32.900000),[], 40),
  ("village_151","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.230000, 102.800000),[], 40),
  ("village_152","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.780000, 100.790000),[], 40),
####fysg_JL


  
  ("salt_mine","Salt_Mine",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.2, -31),[]),
  ("four_ways_inn","Four_Ways_Inn",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.8, -39.6),[]),
  ("test_scene","test_scene",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(22.032110,-2.570555),[]),
  #("test_scene","test_scene",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  ("battlefields","battlefields",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -16.6),[]),
  ("dhorak_keep","Dhorak_Keep",icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50,-58),[]),
  ("xijuan","xijuan",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.12, 166.22),[]),
  ("gengluoguo","gengluoguo",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,( -118.44, 4.36),[]),
  ("duimaguo","duimaguo",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,( -139.45, 12.11),[]),
  ("penglaidaonew","penglaidaonew",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-62.48, -43.13),[]),
  ("liuqiu","liuqiu",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-125.95, 72.66),[]),
  ("moluguo","moluguo",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-153.37, 2.64),[]),
  ("yemataiguo","yemataiguo",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-204.54, -4.57),[]),
  
  ("training_ground","Training Ground",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3, -7),[]),

  ("training_ground_1", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(37.4, 102.8),[], 100),
  ("training_ground_2", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.8, 33),[], 100),
  ("training_ground_3", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.5, 72.0),[], 100),
  ("training_ground_4", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.5, -75.2),[], 100),
  ("training_ground_5", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45.294949, -0.374939),[], 100),
  

#  bridge_a
  ("Bridge_1","{!}1",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.892651, 103.481400),[], -0.201907 * (180.0 / 3.1415926)),
  ("Bridge_2","{!}2",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(55.649342, 44.641788),[], -1.255299 * (180.0 / 3.1415926)),
  ("Bridge_3","{!}3",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62.447300, 92.445549),[], -0.489263 * (180.0 / 3.1415926)),
  ("Bridge_4","{!}4",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(104.341003, 72.008949),[], -1.572176 * (180.0 / 3.1415926)),
  ("Bridge_5","{!}5",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(29.063370, -64.791443),[], 1.265246 * (180.0 / 3.1415926)),
  ("Bridge_6","{!}6",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.385338, 58.114731),[], -1.282817 * (180.0 / 3.1415926)),
  ("Bridge_7","{!}7",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.445141, 65.460037),[], -2.602011 * (180.0 / 3.1415926)),
  ("Bridge_8","{!}8",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.850281, -19.115900),[], 0.540020 * (180.0 / 3.1415926)),
  ("Bridge_9","{!}9",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34.862629, -30.395691),[], -1.089223 * (180.0 / 3.1415926)),
  ("Bridge_10","{!}10",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85.633110, -88.796547),[], -1.849166 * (180.0 / 3.1415926)),
  ("Bridge_11","{!}11",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.702841, 98.424629),[], 2.098953 * (180.0 / 3.1415926)),
  ("Bridge_12","{!}12",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-108.606697, -75.667053),[], -0.619592 * (180.0 / 3.1415926)),
  ("Bridge_13","{!}13",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.316662, -31.446230),[], 1.041077 * (180.0 / 3.1415926)),
  ("Bridge_14","{!}14",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40.957199, 22.659281),[], 0.297390 * (180.0 / 3.1415926)),
  ("Bridge_15","{!}15",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.857199, 12.059281),[], 1.007390 * (180.0 / 3.1415926)),
  ("Bridge_16","{!}16",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.457199, 34.059281),[], 1.217390 * (180.0 / 3.1415926)),
  ("Bridge_17","{!}17",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.455800, 14.537000),[], -0.497390 * (180.0 / 3.1415926)),

  ("looter_spawn_point"   ,"{!}looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(26, 77),[(trp_looter,15,0)]),
  ("steppe_bandit_spawn_point"  ,"the steppes",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(75.830688, 27.696270),[(trp_looter,15,0)]),
  ("taiga_bandit_spawn_point"   ,"the tundra",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(70.000000, 84.000000),[(trp_looter,15,0)]),
##  ("black_khergit_spawn_point"  ,"black_khergit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(47.1, -73.3),[(trp_looter,15,0)]),
  ("forest_bandit_spawn_point"  ,"the forests",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-35, 18),[(trp_looter,15,0)]),
  ("mountain_bandit_spawn_point","the highlands",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(7.258667, -22.694300),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_1"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(48.5, 110),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_2"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-42, 76.7),[(trp_looter,15,0)]),
  ("desert_bandit_spawn_point"  ,"the deserts",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-22.090389, 5.169518),[(trp_looter,15,0)]),
 # add extra towns before this point 
  ("spawn_points_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_2"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_3"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_4"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_5"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ]
