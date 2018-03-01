from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
  ("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
  ("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,0,4)]),

  ("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

##  ("vaegir_nobleman","Vaegir Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_vaegir_knight,2,6),(trp_vaegir_horseman,4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_swadian_knight,2,6),(trp_swadian_man_at_arms,4,12)]),
# Ryan BEGIN
  ("looters","Looters",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_looter,3,45)]),
# Ryan END
  ("manhunters","Manhunters",icon_gray_knight,0,fac_manhunters,soldier_personality,[(trp_manhunter,9,40)]),
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),

#  ("black_khergit_raiders","Black Khergit Raiders",icon_khergit_horseman_b|carries_goods(2),0,fac_black_khergits,bandit_personality,[(trp_black_khergit_guard,1,10),(trp_black_khergit_horseman,5,5)]),
  ("steppe_bandits","Steppe Bandits",icon_khergit|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_steppe_bandit,4,58)]),
  ("taiga_bandits","Tundra Bandits",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_taiga_bandit,4,58)]),
  ("desert_bandits","Desert Bandits",icon_vaegir_knight|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_desert_bandit,4,58)]),
  ("forest_bandits","Forest Bandits",icon_axeman|carries_goods(2),0,fac_forest_bandits,bandit_personality,[(trp_forest_bandit,4,52)]),
  ("mountain_bandits","Mountain Bandits",icon_axeman|carries_goods(2),0,fac_mountain_bandits,bandit_personality,[(trp_mountain_bandit,4,60)]),
  ("sea_raiders","Sea Raiders",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_sea_raider,5,50)]),

  ("deserters","Deserters",icon_vaegir_knight|carries_goods(3),0,fac_deserters,bandit_personality,[]),
    
  ("merchant_caravan","Merchant Caravan",icon_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
  ("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,14,55)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
  ("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

  ("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,5,10),(trp_peasant_woman,3,8)]),

  ("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,5,11)]),
  ("runaway_serfs","Runaway Serfs",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
  ("spy", "Ordinary Townsman", icon_gray_knight|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),
##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
##  ("peasant_rebels", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,bandit_personality,[(trp_peasant_rebel,33,97)]),
##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),

  ("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("patrol_party","Patrol",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),
#  ("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
  ("messenger_party","Messenger",icon_gray_knight|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
  ("kingdom_caravan_party","Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,12,40)]),
  ("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

  ("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),


# Caravans
  ("center_reinforcements","Reinforcements",icon_axeman|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_townsman,5,30),(trp_watchman,4,20)]),  

  ("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  
# Reinforcements
  # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
  # less-modernised templates are generally includes 7-14 troops in total, 
  # med-modernised templates are generally includes 5-10 troops in total, 
  # high-modernised templates are generally includes 3-5 troops in total

  ("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_recruit,5,10),(trp_swadian_militia,2,4),(trp_swadian_wuyingwuwei,2,4),(trp_swadian_wuyingxiaoqi,2,4)]),
  ("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swadian_footman,3,6),(trp_swadian_skirmisher,2,4),(trp_swadian_wuyingyouji,2,4)]),
  ("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_man_at_arms,2,4),(trp_swadian_crossbowman,1,2),(trp_swadian_qiangnushou,2,4)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  ("kingdom_1_reinforcements_d", "{!}kingdom_1_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_dianwei,1,1),(trp_xunyou,1,1),(trp_caoang,1,1),(trp_swadian_huweijun,50,70),(trp_swadian_militia,20,40),(trp_swadian_wuyingwuwei,20,40)]),
  ("kingdom_1_reinforcements_e", "{!}kingdom_1_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_swadian_huweijun,20,40),(trp_swadian_huweijianke,20,40),(trp_swadian_skirmisher,20,40),(trp_swadian_wuyingyouji,20,40),(trp_swadian_militia,20,40),(trp_swadian_wuyingwuwei,20,40)]),
  ("kingdom_1_reinforcements_f", "{!}kingdom_1_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_hanhao,1,1),(trp_swadian_qingzhoubing,30,50),(trp_swadian_skirmisher,20,40),(trp_swadian_wuyingyouji,20,40),(trp_swadian_militia,20,40),(trp_swadian_wuyingwuwei,20,40)]),
  ("kingdom_1_reinforcements_g", "{!}kingdom_1_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_xiahoushang,1,1),(trp_swadian_militia,30,50),(trp_swadian_skirmisher,20,40),(trp_swadian_wuyingyouji,20,40),(trp_swadian_militia,20,40),(trp_swadian_wuyingwuwei,20,40)]),
  ("kingdom_1_reinforcements_h", "{!}kingdom_1_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_caotai,1,1),(trp_niujin,1,1),(trp_wangshuang,1,1),(trp_swadian_militia,30,50),(trp_swadian_skirmisher,20,40),(trp_swadian_wuyingyouji,20,40)]),
  ("kingdom_1_reinforcements_i", "{!}kingdom_1_reinforcements_i", 0, 0, fac_commoners, 0, [(trp_swadian_hubaoqi,30,50),(trp_swadian_militia,30,50),(trp_swadian_skirmisher,20,40),(trp_swadian_wuyingyouji,20,40),(trp_swadian_militia,20,40),(trp_swadian_wuyingwuwei,20,40)]),
  ("kingdom_1_reinforcements_j", "{!}kingdom_1_reinforcements_j", 0, 0, fac_commoners, 0, [(trp_swadian_hubaoqi,30,50),(trp_swadian_militia,30,50),(trp_swadian_skirmisher,20,40),(trp_swadian_wuyingyouji,20,40),(trp_swadian_militia,20,40),(trp_swadian_wuyingwuwei,20,40)]),
  ("kingdom_1_reinforcements_k", "{!}kingdom_1_reinforcements_k", 0, 0, fac_commoners, 0, [(trp_lelin,1,1),(trp_swadian_xiandeng,30,50),(trp_swadian_skirmisher,20,40),(trp_swadian_wuyingyouji,20,40),(trp_swadian_militia,20,40),(trp_swadian_wuyingwuwei,20,40)]),
  ("kingdom_1_reinforcements_l", "{!}kingdom_1_reinforcements_l", 0, 0, fac_commoners, 0, [(trp_lizheng,1,1),(trp_swadian_militia,30,50),(trp_swadian_skirmisher,20,40),(trp_swadian_wuyingyouji,20,40),(trp_swadian_militia,20,40),(trp_swadian_wuyingwuwei,20,40)]),
  ("kingdom_1_reinforcements_m", "{!}kingdom_1_reinforcements_m", 0, 0, fac_commoners, 0, [(trp_zhangji1,1,1),(trp_swadian_militia,30,50),(trp_swadian_skirmisher,20,40),(trp_swadian_wuyingyouji,20,40),(trp_swadian_militia,20,40),(trp_swadian_wuyingwuwei,20,40)]),
  ("kingdom_1_reinforcements_n", "{!}kingdom_1_reinforcements_n", 0, 0, fac_commoners, 0, [(trp_luzhao,1,1),(trp_swadian_militia,30,50),(trp_swadian_skirmisher,20,40),(trp_swadian_wuyingyouji,20,40),(trp_swadian_militia,20,40),(trp_swadian_wuyingwuwei,20,40)]),
  ("kingdom_1_reinforcements_o", "{!}kingdom_1_reinforcements_o", 0, 0, fac_commoners, 0, [(trp_guozu,1,1),(trp_gongsundu,1,1),(trp_swadian_taishanqunkou,50,150),(trp_swadian_skirmisher,20,40),(trp_swadian_wuyingyouji,20,40),(trp_swadian_wuyingwuwei,20,40)]),
  
  ("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_recruit,5,10),(trp_vaegir_footman,2,4),(trp_vaegir_wudanghubu,2,4)]),
  ("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_veteran,2,4),(trp_vaegir_skirmisher,2,4),(trp_vaegir_footman,1,2),(trp_vaegir_zhugeliannu,1,2),(trp_vaegir_wudanghuqi,1,2)]),
  ("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_horseman,2,3),(trp_vaegir_infantry,1,2),(trp_vaegir_yuanrongqishe,1,2)]),
  ("kingdom_2_reinforcements_d", "{!}kingdom_2_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_knight_mod_35,1,1),(trp_knight_mod_36,1,1),(trp_vaegir_baierjingbing,10,20),(trp_vaegir_skirmisher,20,40),(trp_vaegir_footman,10,20),(trp_vaegir_zhugeliannu,10,20)]),
  ("kingdom_2_reinforcements_e", "{!}kingdom_2_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_knight_mod_37,1,1),(trp_knight_2_8,1,1),(trp_vaegir_yuanrongqishe,10,20),(trp_vaegir_skirmisher,20,40),(trp_vaegir_footman,10,20),(trp_vaegir_zhugeliannu,10,20)]),
  ("kingdom_2_reinforcements_f", "{!}kingdom_2_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_knight_mod_38,1,1),(trp_knight_mod_39,1,1),(trp_vaegir_yuanrongqishe,10,20),(trp_vaegir_skirmisher,20,40),(trp_vaegir_footman,10,20),(trp_vaegir_zhugeliannu,10,20)]),
  ("kingdom_2_reinforcements_g", "{!}kingdom_2_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_knight_mod_40,1,1),(trp_knight_2_19,1,1),(trp_vaegir_yuanrongqishe,10,20),(trp_vaegir_skirmisher,20,40),(trp_vaegir_footman,10,20),(trp_vaegir_zhugeliannu,10,20)]),
  
  ("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_tribesman,3,5),(trp_khergit_skirmisher,4,9),(trp_khergit_xiandengsishi,4,9)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,2,4),(trp_khergit_horse_archer,2,4),(trp_khergit_qiangnushou,1,2),(trp_khergit_skirmisher,1,2),(trp_khergit_jingruiqibing,1,2)]),
  ("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,2,4),(trp_khergit_veteran_horse_archer,2,3),(trp_khergit_yandaiqishe,2,3)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
  ("kingdom_3_reinforcements_d", "{!}kingdom_3_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_lvxiang,1,1),(trp_knight_3_19,1,1),(trp_mengdai,1,1),(trp_khergit_yandaiqishe,20,30),(trp_khergit_skirmisher,40,50),(trp_khergit_xiandengsishi,40,50)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
  ("kingdom_3_reinforcements_e", "{!}kingdom_3_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_juhao,1,1),(trp_khergit_veteran_horse_archer,20,30),(trp_khergit_yandaiqishe,20,30),(trp_khergit_skirmisher,40,50),(trp_khergit_xiandengsishi,40,50)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
  ("kingdom_3_reinforcements_f", "{!}kingdom_3_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_khergit_dajishi,20,40),(trp_khergit_veteran_horse_archer,20,30),(trp_khergit_yandaiqishe,20,30),(trp_khergit_skirmisher,40,50),(trp_khergit_xiandengsishi,40,50)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
  ("kingdom_3_reinforcements_g", "{!}kingdom_3_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_gaorou,1,1),(trp_khergit_veteran_horse_archer,20,30),(trp_khergit_yandaiqishe,20,30),(trp_khergit_skirmisher,40,50),(trp_khergit_xiandengsishi,40,50)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
  ("kingdom_3_reinforcements_h", "{!}kingdom_3_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_mayan,1,1),(trp_zhangqiye,1,1),(trp_khergit_yandaiqishe,20,30)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
  ("kingdom_3_reinforcements_i", "{!}kingdom_3_reinforcements_i", 0, 0, fac_commoners, 0, [(trp_zhangnan,1,1),(trp_jiaochu,1,1),(trp_khergit_yandaiqishe,20,30),(trp_khergit_skirmisher,40,50),(trp_khergit_xiandengsishi,40,50)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
  ("kingdom_3_reinforcements_j", "{!}kingdom_3_reinforcements_j", 0, 0, fac_commoners, 0, [(trp_knight_3_11,1,1),(trp_knight_3_12,1,1),(trp_xinpin,1,1),(trp_khergit_yandaiqishe,20,30),(trp_khergit_skirmisher,40,50),(trp_khergit_xiandengsishi,40,50)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
  ("kingdom_3_reinforcements_k", "{!}kingdom_3_reinforcements_k", 0, 0, fac_commoners, 0, [(trp_shenrong,1,1),(trp_khergit_veteran_horse_archer,20,30),(trp_khergit_yandaiqishe,20,30),(trp_khergit_skirmisher,40,50),(trp_khergit_xiandengsishi,40,50)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
  ("kingdom_3_reinforcements_l", "{!}kingdom_3_reinforcements_l", 0, 0, fac_commoners, 0, [(trp_wayuanjin,1,1),(trp_hanlvzi,1,1),(trp_lvweiheng,1,1),(trp_khergit_yandaiqishe,20,30),(trp_khergit_skirmisher,40,50),(trp_khergit_xiandengsishi,40,50)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
  
  ("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_footman,5,10),(trp_nord_recruit,2,4),(trp_nord_danyangjingbing,2,4),(trp_nord_jiefanbing,2,4)]),
  ("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_huntsman,2,5),(trp_nord_archer,2,3),(trp_nord_footman,1,2),(trp_nord_wusheli,1,2),(trp_nord_suweihuqi,1,2)]),
  ("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_warrior,3,5),(trp_nord_wunangongqi,1,2)]),
  ("kingdom_4_reinforcements_d", "{!}kingdom_4_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_dengji,1,1),(trp_liuke,1,1),(trp_nord_wunangongqi,10,20),(trp_nord_recruit,20,40),(trp_nord_danyangjingbing,20,40),(trp_nord_jiefanbing,20,40)]),
  ("kingdom_4_reinforcements_e", "{!}kingdom_4_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_wangwei,1,1),(trp_nord_wunangongqi,10,20),(trp_nord_recruit,20,40),(trp_nord_danyangjingbing,20,40),(trp_nord_jiefanbing,20,40)]),
  ("kingdom_4_reinforcements_f", "{!}kingdom_4_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_likui,1,1),(trp_nord_wunangongqi,10,20),(trp_nord_recruit,20,40),(trp_nord_danyangjingbing,20,40),(trp_nord_jiefanbing,20,40)]),
  ("kingdom_4_reinforcements_g", "{!}kingdom_4_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_pangji,1,1),(trp_zhanghu1,1,1),(trp_chensheng,1,1),(trp_nord_wunangongqi,10,20),(trp_nord_danyangjingbing,20,40),(trp_nord_jiefanbing,20,40)]),
  ("kingdom_4_reinforcements_h", "{!}kingdom_4_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_hanxi,1,1),(trp_nord_changmaojun,10,20),(trp_nord_recruit,20,40),(trp_nord_danyangjingbing,20,40),(trp_nord_jiefanbing,20,40)]),
  ("kingdom_4_reinforcements_i", "{!}kingdom_4_reinforcements_i", 0, 0, fac_commoners, 0, [(trp_huangshe,1,1),(trp_lvgong,1,1),(trp_sufei,1,1),(trp_nord_wunangongqi,10,20),(trp_nord_danyangjingbing,20,40),(trp_nord_jiefanbing,20,40)]),
  ("kingdom_4_reinforcements_j", "{!}kingdom_4_reinforcements_j", 0, 0, fac_commoners, 0, [(trp_caizhong,1,1),(trp_caihe,1,1),(trp_caixun,1,1),(trp_nord_wunangongqi,10,20),(trp_nord_danyangjingbing,20,40),(trp_nord_jiefanbing,20,40)]),
  ("kingdom_4_reinforcements_k", "{!}kingdom_4_reinforcements_k", 0, 0, fac_commoners, 0, [(trp_liuxian,1,1),(trp_jingdaorong,1,1),(trp_nord_wunangongqi,10,20),(trp_nord_danyangjingbing,20,40),(trp_nord_jiefanbing,20,40)]),
  ("kingdom_4_reinforcements_l", "{!}kingdom_4_reinforcements_l", 0, 0, fac_commoners, 0, [(trp_chenying,1,1),(trp_baolong,1,1),(trp_nord_wunangongqi,10,20),(trp_nord_danyangjingbing,20,40),(trp_nord_jiefanbing,20,40)]),
  ("kingdom_4_reinforcements_m", "{!}kingdom_4_reinforcements_m", 0, 0, fac_commoners, 0, [(trp_gongzhi,1,1),(trp_nord_wunangongqi,10,20),(trp_nord_recruit,20,40),(trp_nord_danyangjingbing,20,40),(trp_nord_jiefanbing,20,40)]),
  ("kingdom_4_reinforcements_n", "{!}kingdom_4_reinforcements_n", 0, 0, fac_commoners, 0, [(trp_zhangyi,1,1),(trp_nord_wunangongqi,10,20),(trp_nord_recruit,20,40),(trp_nord_danyangjingbing,20,40),(trp_nord_jiefanbing,20,40)]),
  ("kingdom_4_reinforcements_o", "{!}kingdom_4_reinforcements_o", 0, 0, fac_commoners, 0, [(trp_nord_jinfanzei,10,30),(trp_nord_wunangongqi,10,20),(trp_nord_recruit,20,40),(trp_nord_danyangjingbing,20,40),(trp_nord_jiefanbing,20,40)]),
  
  ("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_tribesman,5,10),(trp_rhodok_spearman,2,4),(trp_rhodok_danyangjingbing,2,4),(trp_rhodok_jiefanbing,2,4)]),
  ("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_crossbowman,3,6),(trp_rhodok_trained_crossbowman,2,4),(trp_rhodok_wusheli,2,4),(trp_rhodok_suweihuqi,2,4)]),
  ("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_veteran_spearman,2,3),(trp_rhodok_veteran_crossbowman,1,2),(trp_rhodok_wunangongqi,1,2)]), 
  ("kingdom_5_reinforcements_d", "{!}kingdom_5_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_dengdang,1,1),(trp_xukun,1,1),(trp_songqian,1,1),(trp_rhodok_wunangongqi,10,20),(trp_rhodok_danyangjingbing,20,40),(trp_rhodok_jiefanbing,20,40)]), 
  ("kingdom_5_reinforcements_e", "{!}kingdom_5_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_knight_5_14,1,1),(trp_jiahua,1,1),(trp_rhodok_wunangongqi,10,20),(trp_rhodok_danyangjingbing,20,40),(trp_rhodok_jiefanbing,20,40)]), 
  ("kingdom_5_reinforcements_f", "{!}kingdom_5_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_chengzi,1,1),(trp_rhodok_veteran_crossbowman,10,20),(trp_rhodok_wunangongqi,10,20),(trp_rhodok_danyangjingbing,20,40),(trp_rhodok_jiefanbing,20,40)]), 
  ("kingdom_5_reinforcements_g", "{!}kingdom_5_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_huangbing,1,1),(trp_rhodok_veteran_crossbowman,10,20),(trp_rhodok_wunangongqi,10,20),(trp_rhodok_danyangjingbing,20,40),(trp_rhodok_jiefanbing,20,40)]), 
  ("kingdom_5_reinforcements_h", "{!}kingdom_5_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_hanzong,1,1),(trp_rhodok_jiefanbing,10,20),(trp_rhodok_wunangongqi,10,20),(trp_rhodok_danyangjingbing,20,40),(trp_rhodok_jiefanbing,20,40)]), 
  ("kingdom_5_reinforcements_i", "{!}kingdom_5_reinforcements_i", 0, 0, fac_commoners, 0, [(trp_zhuran,1,1),(trp_rhodok_veteran_crossbowman,10,20),(trp_rhodok_wunangongqi,10,20),(trp_rhodok_danyangjingbing,20,40),(trp_rhodok_jiefanbing,20,40)]), 
  ("kingdom_5_reinforcements_j", "{!}kingdom_5_reinforcements_j", 0, 0, fac_commoners, 0, [(trp_xuyi,1,1),(trp_rhodok_veteran_crossbowman,10,20),(trp_rhodok_wunangongqi,10,20),(trp_rhodok_danyangjingbing,20,40),(trp_rhodok_jiefanbing,20,40)]), 
  ("kingdom_5_reinforcements_k", "{!}kingdom_5_reinforcements_k", 0, 0, fac_commoners, 0, [(trp_sunfen,1,1),(trp_sunfu,1,1),(trp_rhodok_danyangjingbing,10,20),(trp_rhodok_danyangjingbing,20,40),(trp_rhodok_jiefanbing,20,40)]), 
  ("kingdom_5_reinforcements_l", "{!}kingdom_5_reinforcements_l", 0, 0, fac_commoners, 0, [(trp_rhodok_danyangjingbing,20,30),(trp_rhodok_veteran_crossbowman,10,20),(trp_rhodok_wunangongqi,10,20),(trp_rhodok_danyangjingbing,20,40),(trp_rhodok_jiefanbing,20,40)]), 
  ("kingdom_5_reinforcements_m", "{!}kingdom_5_reinforcements_m", 0, 0, fac_commoners, 0, [(trp_rhodok_danyangjingbing,20,30),(trp_rhodok_veteran_crossbowman,10,20),(trp_rhodok_wunangongqi,10,20),(trp_rhodok_danyangjingbing,20,40),(trp_rhodok_jiefanbing,20,40)]), 
  
  ("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gongsunzan_tribesman,3,5),(trp_gongsunzan_skirmisher,4,9),(trp_gongsunzan_jingruidaofushou,4,9),(trp_gongsunzan_jingruijibing,4,9)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gongsunzan_horseman,2,4),(trp_gongsunzan_horse_archer,2,4),(trp_gongsunzan_skirmisher,1,2),(trp_gongsunzan_jingruigongbing,1,2),(trp_gongsunzan_jingruiqibing,1,2)]),
  ("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gongsunzan_horseman,2,4),(trp_gongsunzan_veteran_horse_archer,2,3)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
  ("kingdom_6_reinforcements_d", "{!}kingdom_6_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_wence,1,1),(trp_zhangji,1,1),(trp_gongsunzan_jingruigongqi,20,30),(trp_gongsunzan_skirmisher,40,50),(trp_gongsunzan_jingruidaofushou,40,50),(trp_gongsunzan_jingruijibing,40,50)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
  ("kingdom_6_reinforcements_e", "{!}kingdom_6_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_gongsunzan_horseman,10,15),(trp_gongsunzan_veteran_horse_archer,20,30),(trp_gongsunzan_jingruigongqi,20,30),(trp_gongsunzan_skirmisher,40,50),(trp_gongsunzan_jingruidaofushou,40,50),(trp_gongsunzan_jingruijibing,40,50)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
  ("kingdom_6_reinforcements_f", "{!}kingdom_6_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_gongsunzan_horseman,10,15),(trp_gongsunzan_veteran_horse_archer,20,30),(trp_gongsunzan_jingruigongqi,20,30),(trp_gongsunzan_skirmisher,40,50),(trp_gongsunzan_jingruidaofushou,40,50),(trp_gongsunzan_jingruijibing,40,50)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
  
  ("kingdom_7_reinforcements_a", "{!}kingdom_7_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_xishu_recruit,5,10),(trp_xishu_footman,2,4),(trp_xishu_jingruiqiangbing,2,4)]),
  ("kingdom_7_reinforcements_b", "{!}kingdom_7_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_xishu_veteran,2,4),(trp_xishu_skirmisher,2,4),(trp_xishu_yizhouqiangnubing,1,2),(trp_xishu_footman,1,2),(trp_xishu_jingruiqibing,1,2)]),
  ("kingdom_7_reinforcements_c", "{!}kingdom_7_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_xishu_horseman,2,3),(trp_xishu_infantry,1,2),(trp_xishu_jingruigongqi,1,2)]),
  ("kingdom_7_reinforcements_d", "{!}kingdom_7_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_knight_mod_15,1,1),(trp_wanglei,1,1),(trp_xishu_dongzhoubing,10,20),(trp_xishu_yizhouqiangnubing,10,20),(trp_xishu_footman,10,20),(trp_xishu_jingruiqibing,10,20)]),
  ("kingdom_7_reinforcements_e", "{!}kingdom_7_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_liugui,1,1),(trp_xishu_infantry,10,20),(trp_xishu_jingruigongqi,10,20),(trp_xishu_yizhouqiangnubing,10,20),(trp_xishu_footman,10,20),(trp_xishu_jingruiqibing,10,20)]),
  ("kingdom_7_reinforcements_f", "{!}kingdom_7_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_pangle,1,1),(trp_liyi,1,1),(trp_xishu_jingruigongqi,10,20),(trp_xishu_yizhouqiangnubing,10,20),(trp_xishu_footman,10,20),(trp_xishu_jingruiqibing,10,20)]),
  ("kingdom_7_reinforcements_g", "{!}kingdom_7_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_dengzhi,1,1),(trp_chengji,1,1),(trp_chengyu,1,1),(trp_xishu_jingruigongqi,10,20),(trp_xishu_footman,10,20),(trp_xishu_jingruiqibing,10,20)]),
  ("kingdom_7_reinforcements_h", "{!}kingdom_7_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_wuban,1,1),(trp_leitong,1,1),(trp_wulan,1,1),(trp_xishu_jingruigongqi,10,20),(trp_xishu_footman,10,20),(trp_xishu_jingruiqibing,10,20)]),
  ("kingdom_7_reinforcements_i", "{!}kingdom_7_reinforcements_i", 0, 0, fac_commoners, 0, [(trp_dengxian,1,1),(trp_lengbao,1,1),(trp_xishu_jingruigongqi,10,20),(trp_xishu_footman,10,20),(trp_xishu_jingruiqibing,10,20)]),
  ("kingdom_7_reinforcements_j", "{!}kingdom_7_reinforcements_j", 0, 0, fac_commoners, 0, [(trp_knight_mod_16,1,1),(trp_xishu_baishuibing,10,20),(trp_xishu_jingruigongqi,10,20),(trp_xishu_footman,10,20),(trp_xishu_jingruiqibing,10,20)]),
  
  ("kingdom_8_reinforcements_a", "{!}kingdom_8_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_mateng_recruit,5,10),(trp_mateng_footman,2,4),(trp_mateng_yulinjunzhen1,2,4),(trp_mateng_yulinjunzhen2,2,4)]),
  ("kingdom_8_reinforcements_b", "{!}kingdom_8_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_mateng_skirmisher,2,4),(trp_mateng_veteran_footman,2,3),(trp_mateng_footman,1,3),(trp_mateng_yulinjunzhen3,1,3),(trp_mateng_xiliangtieqi,1,3)]),
  ("kingdom_8_reinforcements_c", "{!}kingdom_8_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_mateng_horseman,3,5),(trp_mateng_qianglinaggongqi,1,3)]),
  ("kingdom_8_reinforcements_d", "{!}kingdom_8_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_matie,1,1),(trp_maxiu,1,1),(trp_mateng_qianglinaggongqi,10,30),(trp_mateng_footman,20,40),(trp_mateng_yulinjunzhen1,20,40),(trp_mateng_yulinjunzhen2,20,40)]),
  
  ("kingdom_9_reinforcements_a", "{!}kingdom_9_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_yuanshu_recruit,5,10),(trp_yuanshu_militia,2,4),(trp_yuanshu_jingruidaopaishou,2,4),(trp_yuanshu_jingruiqiangbing,2,4)]),
  ("kingdom_9_reinforcements_b", "{!}kingdom_9_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_yuanshu_footman,3,6),(trp_yuanshu_skirmisher,2,4),(trp_yuanshu_jingruinubing,2,4),(trp_yuanshu_jingruiqibing,2,4)]),
  ("kingdom_9_reinforcements_c", "{!}kingdom_9_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_yuanshu_man_at_arms,2,4),(trp_yuanshu_crossbowman,1,2),(trp_yuanshu_jingruigongqi,1,2)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  ("kingdom_9_reinforcements_d", "{!}kingdom_9_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_knight_mod_27,1,1),(trp_knight_mod_28,1,1),(trp_yuanshu_jingruigongqi,10,20),(trp_yuanshu_militia,20,40),(trp_yuanshu_jingruidaopaishou,20,40),(trp_yuanshu_jingruiqiangbing,20,40)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  ("kingdom_9_reinforcements_e", "{!}kingdom_9_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_knight_1_19,1,1),(trp_yuanshu_crossbowman,10,20),(trp_yuanshu_jingruigongqi,10,20),(trp_yuanshu_militia,20,40),(trp_yuanshu_jingruidaopaishou,20,40),(trp_yuanshu_jingruiqiangbing,20,40)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  ("kingdom_9_reinforcements_f", "{!}kingdom_9_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_xunzheng,1,1),(trp_chenlan,1,1),(trp_yuanshu_jingruigongqi,10,20),(trp_yuanshu_militia,20,40),(trp_yuanshu_jingruidaopaishou,20,40),(trp_yuanshu_jingruiqiangbing,20,40)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  
  ("kingdom_10_reinforcements_a", "{!}kingdom_10_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_lvbu_recruit,5,10),(trp_lvbu_footman,2,4)]),
  ("kingdom_10_reinforcements_b", "{!}kingdom_10_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_lvbu_skirmisher,2,4),(trp_lvbu_veteran_footman,2,3),(trp_lvbu_jingruinubing,1,3),(trp_lvbu_footman,1,3),(trp_lvbu_xiliangtieqi,1,3)]),
  ("kingdom_10_reinforcements_c", "{!}kingdom_10_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_lvbu_horseman,3,5),(trp_lvbu_jingruigongqi,1,3)]),
  ("kingdom_10_reinforcements_d", "{!}kingdom_10_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_chenglian,1,1),(trp_lifeng,1,1),(trp_xuelan,1,1),(trp_lvbu_wenhouqingqi,10,30),(trp_lvbu_veteran_footman,20,30),(trp_lvbu_jingruinubing,10,30)]),
  ("kingdom_10_reinforcements_e", "{!}kingdom_10_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_changxi,1,1),(trp_sunguan,1,1),(trp_wudun,1,1),(trp_lvbu_taishanbing,10,30),(trp_lvbu_veteran_footman,20,30),(trp_lvbu_jingruinubing,10,30)]),
  ("kingdom_10_reinforcements_f", "{!}kingdom_10_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_zhangchao,1,1),(trp_lvbu_jingruigongqi,10,30),(trp_lvbu_veteran_footman,20,30),(trp_lvbu_jingruinubing,10,30),(trp_lvbu_footman,10,30),(trp_lvbu_xiliangtieqi,10,30)]),
  ("kingdom_10_reinforcements_g", "{!}kingdom_10_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_lvbu_horseman,30,50),(trp_lvbu_xianzhenyingjiashi,10,30),(trp_lvbu_veteran_footman,20,30),(trp_lvbu_jingruinubing,10,30),(trp_lvbu_footman,10,30),(trp_lvbu_xiliangtieqi,10,30)]),
  ("kingdom_10_reinforcements_h", "{!}kingdom_10_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_caoxing,1,1),(trp_lvbu_veteran_footman,10,30),(trp_lvbu_veteran_footman,20,30),(trp_lvbu_jingruinubing,10,30),(trp_lvbu_footman,10,30),(trp_lvbu_xiliangtieqi,10,30)]),
  ("kingdom_10_reinforcements_i", "{!}kingdom_10_reinforcements_i", 0, 0, fac_commoners, 0, [(trp_chenjiao,1,1),(trp_lvbu_jingruigongqi,10,30),(trp_lvbu_veteran_footman,20,30),(trp_lvbu_jingruinubing,10,30),(trp_lvbu_footman,10,30),(trp_lvbu_xiliangtieqi,10,30)]),
  ("kingdom_10_reinforcements_j", "{!}kingdom_10_reinforcements_j", 0, 0, fac_commoners, 0, [(trp_zhanghu,1,1),(trp_lvbu_zhongjiajishi,10,30),(trp_lvbu_veteran_footman,20,30),(trp_lvbu_jingruinubing,10,30),(trp_lvbu_footman,10,30),(trp_lvbu_xiliangtieqi,10,30)]),
  ("kingdom_10_reinforcements_k", "{!}kingdom_10_reinforcements_k", 0, 0, fac_commoners, 0, [(trp_lvbu_xianzhenyingjiashi,10,30),(trp_lvbu_jingruigongqi,10,30),(trp_lvbu_veteran_footman,20,30),(trp_lvbu_jingruinubing,10,30),(trp_lvbu_footman,10,30),(trp_lvbu_xiliangtieqi,10,30)]),
  ("kingdom_10_reinforcements_l", "{!}kingdom_10_reinforcements_l", 0, 0, fac_commoners, 0, [(trp_dongzhao,1,1),(trp_yangchou,1,1),(trp_wagu,1,1),(trp_lvbu_footman,10,30),(trp_lvbu_veteran_footman,20,30),(trp_lvbu_jingruinubing,10,30)]),
  
  ("kingdom_11_reinforcements_a", "{!}kingdom_11_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_zhanglu_recruit,5,10),(trp_zhanglu_footman,2,4),(trp_zhanglu_jingruidaopaishou,2,4),(trp_zhanglu_jingruiqiangbing,2,4)]),
  ("kingdom_11_reinforcements_b", "{!}kingdom_11_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_zhanglu_veteran,2,4),(trp_zhanglu_skirmisher,2,4),(trp_zhanglu_footman,1,2),(trp_zhanglu_jingruinubing,1,2),(trp_zhanglu_jingruiqibing,1,2)]),
  ("kingdom_11_reinforcements_c", "{!}kingdom_11_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_zhanglu_horseman,2,3),(trp_zhanglu_infantry,1,2),(trp_zhanglu_jingruigongqi,1,2)]),
  ("kingdom_11_reinforcements_d", "{!}kingdom_11_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_zhangyulan,1,1),(trp_zhangkui,1,1),(trp_zhanglu_jingruigongqi,10,20),(trp_zhanglu_footman,20,40),(trp_zhanglu_jingruidaopaishou,20,40),(trp_zhanglu_jingruiqiangbing,20,40)]),
  ("kingdom_11_reinforcements_e", "{!}kingdom_11_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_yangang,1,1),(trp_yangren,1,1),(trp_zhanglu_jingruigongqi,10,20),(trp_zhanglu_footman,20,40),(trp_zhanglu_jingruidaopaishou,20,40),(trp_zhanglu_jingruiqiangbing,20,40)]),
  
  ("kingdom_12_reinforcements_a", "{!}kingdom_12_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_lijue_recruit,5,10),(trp_lijue_footman,2,4),(trp_lijue_jingruiqiangbing,2,4)]),
  ("kingdom_12_reinforcements_b", "{!}kingdom_12_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_lijue_skirmisher,2,4),(trp_lijue_veteran_footman,2,3),(trp_lijue_footman,1,3),(trp_lijue_jingruigongbing,1,3),(trp_lijue_xiliangtieqi,1,3)]),
  ("kingdom_12_reinforcements_c", "{!}kingdom_12_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_lijue_horseman,3,5),(trp_lijue_jingruigongqi,1,3)]),
  ("kingdom_12_reinforcements_d", "{!}kingdom_12_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_knight_6_5,1,1),(trp_zhangquan,1,1),(trp_hucheer,1,1),(trp_lijue_feixiongjun,10,20),(trp_lijue_footman,20,40),(trp_lijue_jingruiqiangbing,20,40)]),
  ("kingdom_12_reinforcements_e", "{!}kingdom_12_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_lili,1,1),(trp_libi,1,1),(trp_lishi,1,1),(trp_lijue_feixiongjun,10,20),(trp_lijue_footman,20,40),(trp_lijue_jingruiqiangbing,20,40)]),
  ("kingdom_12_reinforcements_f", "{!}kingdom_12_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_wuxi,1,1),(trp_lijue_feixiongjun,10,20),(trp_lijue_veteran_footman,20,30),(trp_lijue_footman,10,30),(trp_lijue_jingruigongbing,10,30),(trp_lijue_xiliangtieqi,10,30)]),
  ("kingdom_12_reinforcements_g", "{!}kingdom_12_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_limeng,1,1),(trp_wangfang,1,1),(trp_lijue_feixiongjun,10,20),(trp_lijue_footman,20,40),(trp_lijue_jingruiqiangbing,20,40)]),
  ("kingdom_12_reinforcements_h", "{!}kingdom_12_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_zuoling,1,1),(trp_lijue_jingruigongqi,10,30),(trp_lijue_veteran_footman,20,30),(trp_lijue_footman,10,30),(trp_lijue_jingruigongbing,10,30),(trp_lijue_xiliangtieqi,10,30)]),
  ("kingdom_12_reinforcements_i", "{!}kingdom_12_reinforcements_i", 0, 0, fac_commoners, 0, [(trp_lile,1,1),(trp_hanbi,1,1),(trp_hucai,1,1),(trp_lijue_jingruigongqi,10,20),(trp_lijue_footman,20,40),(trp_lijue_jingruiqiangbing,20,40)]),
  ("kingdom_12_reinforcements_j", "{!}kingdom_12_reinforcements_j", 0, 0, fac_commoners, 0, [(trp_wuzilan,1,1),(trp_wangfu,1,1),(trp_zhongji,1,1),(trp_lijue_jingruigongqi,10,20),(trp_lijue_footman,20,40),(trp_lijue_jingruiqiangbing,20,40)]),
  ("kingdom_12_reinforcements_k", "{!}kingdom_12_reinforcements_k", 0, 0, fac_commoners, 0, [(trp_shihuan,1,1),(trp_xushang,1,1),(trp_lvjian,1,1),(trp_lijue_jingruigongqi,10,20),(trp_lijue_footman,20,40),(trp_lijue_jingruiqiangbing,20,40)]),
  
  ("kingdom_13_reinforcements_a", "{!}kingdom_13_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gongsundu_tribesman,3,5),(trp_gongsundu_skirmisher,4,9),(trp_gongsundu_jingruidaofushou,4,9),(trp_gongsundu_jingruijibing,4,9)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_13_reinforcements_b", "{!}kingdom_13_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gongsundu_horseman,2,4),(trp_gongsundu_horse_archer,2,4),(trp_gongsundu_skirmisher,1,2),(trp_gongsundu_jingruigongbing,1,2),(trp_gongsundu_yulinqi,1,2)]),
  ("kingdom_13_reinforcements_c", "{!}kingdom_13_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gongsundu_horseman,2,4),(trp_gongsundu_veteran_horse_archer,2,3),(trp_gongsundu_jingruigongqi,2,3)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
  ("kingdom_13_reinforcements_d", "{!}kingdom_13_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_yangyi,1,1),(trp_liuyi,1,1),(trp_liangmao,1,1),(trp_gongsundu_jingruigongqi,20,30),(trp_gongsundu_jingruidaofushou,40,50),(trp_gongsundu_jingruijibing,40,50)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
  ("kingdom_13_reinforcements_e", "{!}kingdom_13_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_gongsunmo,1,1),(trp_zhangchang,1,1),(trp_hanzhong,1,1),(trp_gongsundu_jingruigongqi,20,30),(trp_gongsundu_jingruidaofushou,40,50),(trp_gongsundu_jingruijibing,40,50)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
  
  ("kingdom_14_reinforcements_a", "{!}kingdom_14_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_hansui_recruit,5,10),(trp_hansui_footman,2,4),(trp_hansui_yulinjunzhen1,2,4),(trp_hansui_yulinjunzhen2,2,4)]),
  ("kingdom_14_reinforcements_b", "{!}kingdom_14_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_hansui_skirmisher,2,4),(trp_hansui_veteran_footman,2,3),(trp_hansui_footman,1,3),(trp_hansui_yulinjunzhen3,1,3),(trp_hansui_xiliangtieqi,1,3)]),
  ("kingdom_14_reinforcements_c", "{!}kingdom_14_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_hansui_horseman,3,5),(trp_hansui_qianglinaggongqi,1,3)]),
  ("kingdom_14_reinforcements_d", "{!}kingdom_14_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_yanxing,1,1),(trp_hansui_qianglinaggongqi,10,30),(trp_hansui_veteran_footman,20,30),(trp_hansui_footman,10,30),(trp_hansui_yulinjunzhen3,10,30),(trp_hansui_xiliangtieqi,10,30)]),
  
  ("kingdom_15_reinforcements_a", "{!}kingdom_15_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_liuyao_tribesman,5,10),(trp_liuyao_spearman,2,4),(trp_liuyao_jingruidaopaishou,2,4),(trp_liuyao_jingruiqiangbing,2,4)]),
  ("kingdom_15_reinforcements_b", "{!}kingdom_15_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_liuyao_crossbowman,3,6),(trp_liuyao_trained_crossbowman,2,4),(trp_liuyao_jingruinubing,2,4),(trp_liuyao_jingruiqibing,2,4)]),
  ("kingdom_15_reinforcements_c", "{!}kingdom_15_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_liuyao_veteran_spearman,2,3),(trp_liuyao_veteran_crossbowman,1,2),(trp_liuyao_jingruigongqi,1,2)]), 
  ("kingdom_15_reinforcements_d", "{!}kingdom_15_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_liuji,1,1),(trp_liuyao_veteran_crossbowman,10,20),(trp_liuyao_jingruigongqi,10,20),(trp_liuyao_spearman,20,40),(trp_liuyao_jingruidaopaishou,20,40),(trp_liuyao_jingruiqiangbing,20,40)]), 
  ("kingdom_15_reinforcements_e", "{!}kingdom_15_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_xuzhao,1,1),(trp_daiyuan,1,1),(trp_weilan,1,1),(trp_liuyao_jingruigongqi,10,20),(trp_liuyao_jingruinubing,20,40),(trp_liuyao_jingruiqibing,20,40)]), 
  ("kingdom_15_reinforcements_f", "{!}kingdom_15_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_yufan,1,1),(trp_liuyao_veteran_crossbowman,10,20),(trp_liuyao_jingruigongqi,10,20),(trp_liuyao_jingruinubing,20,40),(trp_liuyao_jingruiqibing,20,40)]), 
  ("kingdom_15_reinforcements_g", "{!}kingdom_15_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_yumi,1,1),(trp_liuyao_veteran_crossbowman,10,20),(trp_liuyao_jingruigongqi,10,20),(trp_liuyao_jingruinubing,20,40),(trp_liuyao_jingruiqibing,20,40)]), 
   
  ("kingdom_16_reinforcements_a", "{!}kingdom_16_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_yanbaihu_tribesman,5,10),(trp_yanbaihu_spearman,2,4),(trp_yanbaihu_jingruidaopaishou,2,4),(trp_yanbaihu_jingruiqiangbing,2,4)]),
  ("kingdom_16_reinforcements_b", "{!}kingdom_16_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_yanbaihu_crossbowman,3,6),(trp_yanbaihu_trained_crossbowman,2,4),(trp_yanbaihu_jingruinubing,2,4),(trp_yanbaihu_jingruiqibing,2,4)]),
  ("kingdom_16_reinforcements_c", "{!}kingdom_16_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_yanbaihu_veteran_spearman,2,3),(trp_yanbaihu_veteran_crossbowman,1,2),(trp_yanbaihu_jingruigongqi,1,2)]), 
  
  ("kingdom_17_reinforcements_a", "{!}kingdom_17_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_kongrong_recruit,5,10),(trp_kongrong_militia,2,4),(trp_kongrong_jingruidaopaishou,2,4),(trp_kongrong_jingruiqiangbing,2,4)]),
  ("kingdom_17_reinforcements_b", "{!}kingdom_17_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_kongrong_footman,3,6),(trp_kongrong_skirmisher,2,4),(trp_kongrong_jingruinubing,2,4),(trp_kongrong_jingruiqibing,2,4)]),
  ("kingdom_17_reinforcements_c", "{!}kingdom_17_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_kongrong_man_at_arms,2,4),(trp_kongrong_crossbowman,1,2),(trp_kongrong_jingruigongqi,1,2)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)

  ("kingdom_18_reinforcements_a", "{!}kingdom_18_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sarranid_recruit,5,10),(trp_sarranid_footman,2,4)]),
  ("kingdom_18_reinforcements_b", "{!}kingdom_18_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sarranid_skirmisher,2,4),(trp_sarranid_veteran_footman,2,3),(trp_sarranid_footman,1,3)]),
  ("kingdom_18_reinforcements_c", "{!}kingdom_18_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sarranid_horseman,3,5)]),

  ("kingdom_19_reinforcements_a", "{!}kingdom_19_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_taoqian_recruit,5,10),(trp_taoqian_militia,2,4),(trp_taoqian_jingruidaopaishou,2,4),(trp_taoqian_jingruiqiangbing,2,4)]),
  ("kingdom_19_reinforcements_b", "{!}kingdom_19_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_taoqian_footman,3,6),(trp_taoqian_skirmisher,2,4),(trp_taoqian_jingruinubing,2,4),(trp_taoqian_jingruiqibing,2,4)]),
  ("kingdom_19_reinforcements_c", "{!}kingdom_19_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_taoqian_man_at_arms,2,4),(trp_taoqian_crossbowman,1,2),(trp_taoqian_jingruigongqi,1,2)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  
##  ("kingdom_1_reinforcements_a", "kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_footman,3,7),(trp_swadian_skirmisher,5,10),(trp_swadian_militia,11,26)]),
##  ("kingdom_1_reinforcements_b", "kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swadian_man_at_arms,5,10),(trp_swadian_infantry,5,10),(trp_swadian_crossbowman,3,8)]),
##  ("kingdom_1_reinforcements_c", "kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_knight,2,6),(trp_swadian_sergeant,2,5),(trp_swadian_sharpshooter,2,5)]),
##
##  ("kingdom_2_reinforcements_a", "kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_veteran,3,7),(trp_vaegir_skirmisher,5,10),(trp_vaegir_footman,11,26)]),
##  ("kingdom_2_reinforcements_b", "kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_horseman,4,9),(trp_vaegir_infantry,5,10),(trp_vaegir_archer,3,8)]),
##  ("kingdom_2_reinforcements_c", "kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_knight,3,7),(trp_vaegir_guard,2,5),(trp_vaegir_marksman,2,5)]),
##
##  ("kingdom_3_reinforcements_a", "kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,3,7),(trp_khergit_skirmisher,5,10),(trp_khergit_tribesman,11,26)]),
##  ("kingdom_3_reinforcements_b", "kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_veteran_horse_archer,4,9),(trp_khergit_horse_archer,5,10),(trp_khergit_horseman,3,8)]),
##  ("kingdom_3_reinforcements_c", "kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_lancer,3,7),(trp_khergit_veteran_horse_archer,2,5),(trp_khergit_horse_archer,2,5)]),
##
##  ("kingdom_4_reinforcements_a", "kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_trained_footman,3,7),(trp_nord_footman,5,10),(trp_nord_recruit,11,26)]),
##  ("kingdom_4_reinforcements_b", "kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_veteran,4,9),(trp_nord_warrior,5,10),(trp_nord_footman,3,8)]),
##  ("kingdom_4_reinforcements_c", "kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_champion,1,3),(trp_nord_veteran,2,5),(trp_nord_warrior,2,5)]),
##
##  ("kingdom_5_reinforcements_a", "kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_spearman,3,7),(trp_rhodok_crossbowman,5,10),(trp_rhodok_tribesman,11,26)]),
##  ("kingdom_5_reinforcements_b", "kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_trained_spearman,4,9),(trp_rhodok_spearman,5,10),(trp_rhodok_crossbowman,3,8)]),
##  ("kingdom_5_reinforcements_c", "kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_sergeant,3,7),(trp_rhodok_veteran_spearman,2,5),(trp_rhodok_veteran_crossbowman,2,5)]),



  ("steppe_bandit_lair" ,"Steppe Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_steppe_bandit,15,58)]),
  ("taiga_bandit_lair","Tundra Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_taiga_bandit,15,58)]),
  ("desert_bandit_lair" ,"Desert Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_desert_bandit,15,58)]),
  ("forest_bandit_lair" ,"Forest Bandit Camp",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_forest_bandit,15,58)]),
  ("mountain_bandit_lair" ,"Mountain Bandit Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_mountain_bandit,15,58)]),
  ("sea_raider_lair","Sea Raider Landing",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_sea_raider,15,50)]),
  ("looter_lair","Kidnappers' Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,25)]),
  
  ("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,50)]),

  ("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),
]
