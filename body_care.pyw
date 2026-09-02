import PySimpleGUI as sg
import datetime
import winsound
import threading
import time
import os
##############################################################
sg.set_options(font=('Courier 12'))
sg.theme('DarkGray2')
settings = sg.UserSettings(path=os.path.dirname(os.path.abspath(__file__)))
icon_base64 = b'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'
FONT_MESSAGE = 'Courier 20'
FONT_INFO = 'Courier 16'
##############################################################

# remind thread 
def remind_thread(to_msg_en, to_beep_en, to_msg, to_duration, to_beep_freq, to_beep_tm):
    if to_msg_en==True:
        sg.popup_quick_message(to_msg, background_color='DarkGreen', text_color='White', keep_on_top=True, font=FONT_MESSAGE,
                               auto_close_duration=to_duration)
    bz_sec = to_duration
    sleep_tm = max((1000 - to_beep_tm) / 1000, 0.1)
    while (bz_sec>0):        
        if to_beep_en==True:
            winsound.Beep(to_beep_freq, to_beep_tm)
        time.sleep(sleep_tm)
        bz_sec -= 1

##############################################################
def make_button_gui():
    col_button = [       
        [sg.B('Reset'), sg.Submit(), sg.Cancel()] # using shortcut for sg.Button('Submit')
    ]
    layout_button = [                
        [sg.Col(col_button, k='col_button', justification="center")]     # 'left', 'right', 'center'     
    ]
    return sg.Col(layout_button, k='layout_button', )

def make_config_gui(eye_alarm_msg, eye_alarm_beep, eye_alarm_beep_freq, eye_alarm_beep_tm, eye_min, eye_sec, eye_msg):
    col_config = [        
        [sg.Text('Remind message:'), sg.In(default_text=eye_msg, key='eye_msg',), ],        
        [sg.CB('Message Alarm', default=eye_alarm_msg, k='eye_alarm_msg'),],                        
        [sg.Text('Beep freq(Hz) :'), sg.Slider(range=(400, 4000), orientation='h', default_value=eye_alarm_beep_freq, size=(45,10), key='eye_alarm_beep_freq')],
        [sg.Text('Beep time(ms) :'), sg.Slider(range=(100, 900), orientation='h', default_value=eye_alarm_beep_tm, size=(45,10), key='eye_alarm_beep_tm')],
        [sg.CB('Beep Alarm ', default=eye_alarm_beep, k='eye_alarm_beep'),],
        [sg.HSep()],
        [sg.Text('Every minute  :'), sg.Slider(range=(1, 60), orientation='h', default_value=eye_min, size=(45,10), key='eye_min')],
        [sg.Text('Break minute  :'), sg.Slider(range=(1, 10), orientation='h', default_value=eye_sec, size=(45,10), key='eye_sec')],        
        
    ]

    frame_config = [        
        [sg.Col(col_config, k='col_config'), ]        
    ]     
    return sg.Frame('Eye Care Configure', frame_config, title_color='pink') 


def make_setting_window(eye_alarm_msg, eye_alarm_beep, eye_alarm_beep_freq, eye_alarm_beep_tm, eye_min, eye_sec, eye_msg):
    layout = [  
               [make_config_gui(eye_alarm_msg, eye_alarm_beep, eye_alarm_beep_freq, eye_alarm_beep_tm, eye_min, eye_sec, eye_msg),], 
               [sg.HSeparator(),],
               [make_button_gui(),],       
             ]
    return sg.Window('Eye 20-20-20 rule configure' , layout, element_justification='c', no_titlebar=True, grab_anywhere=True, keep_on_top=True)
##############################################################    

EYE_MSG_DEFAULT = '起來喝喝水、眼晴動一動、身體動一動'
EYE_MIN_DEFAULT = 20
EYE_SEC_DEFAULT = 1
EYE_MSG_CB_DEFAULT = True
EYE_BEEP_CB_DEFAULT = False
def main():

    eye_alarm_msg = settings.get('eye_alarm_msg', EYE_MSG_CB_DEFAULT)
    eye_alarm_beep = settings.get('eye_alarm_beep', EYE_BEEP_CB_DEFAULT)
    eye_alarm_beep_freq = settings.get('eye_alarm_beep_freq', 1600)
    eye_alarm_beep_tm = settings.get('eye_alarm_beep_tm', 200)
    eye_min = settings.get('eye_min', EYE_MIN_DEFAULT)
    raw_eye_sec = settings.get('eye_sec', EYE_SEC_DEFAULT)
    eye_sec = raw_eye_sec * 60 if raw_eye_sec <= 10 else raw_eye_sec  # migrate old seconds value
    eye_msg = settings.get('eye_msg', EYE_MSG_DEFAULT)
    
    
    tm_alarm_en = False
    next_alarm_time = None
    next_alarm_end = None
    
    window = None
    menu_def = ['X', ['Info', 'Setting', '---', 'Exit']]
    
    tray = sg.SystemTray(menu=menu_def, data_base64=icon_base64)

    while True:  # Event Loop  
        event = tray.read(timeout=100)
        if event == 'Exit':
            break          
        elif event =='Setting' and not window:
            window = make_setting_window(eye_alarm_msg, eye_alarm_beep, eye_alarm_beep_freq, eye_alarm_beep_tm, eye_min, max(eye_sec // 60, 1), eye_msg, )
        elif event in ('Info', sg.EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED):
            alarm_msg  = 'On' if eye_alarm_msg==True else 'Off'
            alarm_beep = 'On' if eye_alarm_beep==True else 'Off'
            clock_str = next_alarm_time.strftime('%H:%M:%S') if next_alarm_time else '--:--:--'
            sg.popup_quick_message( f'1). Remind clock  = {clock_str}', 
                                    f'2). Remind Rule   = {eye_min:02d}min-{eye_sec//60:02d}min', 
                                    f'3). Message Alarm = {alarm_msg}',
                                    f'4). Beep    Alarm = {alarm_beep}', 
                                    f'5). Beep Freq/Tm  = {eye_alarm_beep_freq}/{eye_alarm_beep_tm}',
                                    auto_close_duration = 3, # sec
                                    background_color='light Yellow', text_color='Black', keep_on_top=True, font=FONT_INFO) 
        ##############################################################                 
        if window:
            event, values = window.read(timeout=500)
            if event == 'Reset':
                    window['eye_alarm_msg'].Update(EYE_MSG_CB_DEFAULT)
                    window['eye_alarm_beep'].Update(EYE_BEEP_CB_DEFAULT)
                    window['eye_alarm_beep_freq'].Update(1600)
                    window['eye_alarm_beep_tm'].Update(200)
                    window['eye_min'].Update(EYE_MIN_DEFAULT)
                    window['eye_sec'].Update(EYE_SEC_DEFAULT)
                    window['eye_msg'].Update(EYE_MSG_DEFAULT)
                    
                    continue
            elif event in (sg.WIN_CLOSED, 'Cancel', 'Submit'):                
                ######################################################
                if event == 'Submit':
                    is_restart = False if (int(values['eye_min']) == eye_min and int(values['eye_sec']) == eye_sec) else True                        
                    eye_alarm_msg = values['eye_alarm_msg'] #CB
                    eye_alarm_beep = values['eye_alarm_beep']#CB
                    eye_alarm_beep_freq = int(values['eye_alarm_beep_freq'])
                    eye_alarm_beep_tm = int(values['eye_alarm_beep_tm'])
                    eye_min = int(values['eye_min']) 
                    eye_sec = int(values['eye_sec']) * 60
                    eye_msg = values['eye_msg']
                    if len(eye_msg)==0:
                        window['eye_msg'].Update(EYE_MSG_DEFAULT)
                        sg.popup_quick_message('Reminding message CAN NOT Empty !!!', background_color='light Yellow', text_color='Red', keep_on_top=True, font=FONT_INFO)
                        continue
                    settings['eye_alarm_msg'] =  eye_alarm_msg
                    settings['eye_alarm_beep'] = eye_alarm_beep
                    settings['eye_alarm_beep_freq'] = eye_alarm_beep_freq
                    settings['eye_alarm_beep_tm'] = eye_alarm_beep_tm
                    settings['eye_min'] = eye_min
                    settings['eye_sec'] = int(values['eye_sec'])
                    settings['eye_msg'] = eye_msg
                    if (is_restart==True):
                        next_alarm_time = None
                        next_alarm_end = None
                        tm_alarm_en = False                
                        sg.popup_quick_message('Reminding time will re-start', background_color='light Yellow', text_color='Black', keep_on_top=True, font=FONT_INFO)
                ######################################################
                window.close()
                window = None   
                
        ##############################################################                 
        now = datetime.datetime.now()    
        if next_alarm_time is None:
            next_alarm_time = now + datetime.timedelta(minutes=eye_min, seconds=eye_sec)

        # quiet hours: only lunch 12:00-13:00
        now_hhmm = now.hour * 60 + now.minute
        if now_hhmm >= 12 * 60 and now_hhmm < 13 * 60:
            tm_alarm_en = False
            next_alarm_time = None
            next_alarm_end = None
            continue

        # auto exit after 17:30
        if now_hhmm >= 17 * 60 + 30:
            break

        if not tm_alarm_en:
            if now >= next_alarm_time:
                tm_alarm_en = True
                next_alarm_end = now + datetime.timedelta(seconds=eye_sec)
                t = threading.Thread(target = remind_thread, args=(eye_alarm_msg, eye_alarm_beep, eye_msg, eye_sec, eye_alarm_beep_freq,  eye_alarm_beep_tm))
                t.start()                
        else:
            if now >= next_alarm_end:
                tm_alarm_en = False
                next_alarm_time = now + datetime.timedelta(minutes=eye_min)

        ##############################################################                  
    tray.close()
    if window:
        window.close()   

##############################################################  
main()
