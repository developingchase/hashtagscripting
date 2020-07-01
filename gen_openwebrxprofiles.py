#! python
# Gen OpenWebRX Profiles
# Used to rapidly generate appropriate profiles for use in the Openwebrx config_webrx.py file

# list of sets of start/stop freq ranges
freqs = [[136000000,174000000],[312000000,317000000],[432000000,435000000],[440000000,470000000],[500000000,510000000],[900000000,930000000]]

# uncomment which settings you are using for your device
# rtlsdr settings 
samp_rate = 2400000
rf_gain = 30

# hackrf settings -- still need to add these parameters
# samp_rate = 
# rf_gain = 

start_mod = "nfm"
initial_squelch_level = -35

profiles = {}
for x in freqs:
    cur_start_freq = x[0]
    stop_freq = x[1]
    
    while cur_start_freq < stop_freq:
        prof_dict = {}
        cur_center_freq = int(cur_start_freq + (samp_rate/2))
        prof_name = str(cur_start_freq/1000000) + " - " + str((cur_start_freq + samp_rate)/1000000) + " MHz"
        
        prof_dict["name"] = prof_name 
        prof_dict["start_freq"] = cur_start_freq
        prof_dict["center_freq"] = cur_center_freq 
        prof_dict["samp_rate"] = samp_rate 
        prof_dict["rf_gain"] = rf_gain 
        prof_dict["start_mod"] = start_mod
        prof_dict["initial_squelch_level"] = initial_squelch_level

        profiles[prof_name] = prof_dict 
        
        cur_start_freq += samp_rate 

print("Verify the output here: \n\n")
for profile in profiles:
    print(str(profiles[profile]))
print("\n\nAnd copy and paste this into the config_webrx.py file, in the appropriate place under \"profiles\". Take care to remove the outer brackets and check your syntax. \n")
print(profiles)