<!DOCTYPE html>
<!-- saved from url=(0o115)https://colab.research.google.com/drive/1VqDTvZz0F7fnwYBzWXs7wXvHbMOZqeUB#scrollTo=qkO9TZr3KHuQ -->
<html lang="en" theme="light" editor="Default Light"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta name="og-profile-acct" content="u2004095@student.cuet.ac.bd"><script type="text/javascript" async="" charset="utf-8" src="./main_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-76u17na0CP00vfwMm4sR2Vvs+diG7mwcVdyaONTZPGxfxUgxr51lvGQyQkZQXzHc" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./main_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-76u17na0CP00vfwMm4sR2Vvs+diG7mwcVdyaONTZPGxfxUgxr51lvGQyQkZQXzHc" nonce=""></script><script src="./main_files/cb=gapi.loaded_1" nonce="" async=""></script><script src="./main_files/cb=gapi.loaded_0" nonce="" async=""></script><script async="" src="./main_files/analytics.js.download"></script><script nonce="">
      document.addEventListener('keydown', (e) => {
        // Stop propagation on ESC because otherwise it will halt outbound XHRs
        // See b/131755324 for more info.
        if (e.key === 'Escape') {
          e.stopPropagation();
          e.preventDefault();
        }
      });
    </script><meta name="referrer" content="origin"><meta name="viewport" content="width=device-width, initial-scale=1"><title>main.py - Colab</title><link href="./main_files/css2" rel="stylesheet"><link href="./main_files/css" rel="stylesheet"><link rel="search" type="application/opensearchdescription+xml" href="https://colab.research.google.com/opensearch.xml" title="Google Colab"><style>.gb_3d{font:13px/27px Roboto,Arial,sans-serif;z-index:986}@-webkit-keyframes gb__a{0%{opacity:0}50%{opacity:1}}@keyframes gb__a{0%{opacity:0}50%{opacity:1}}a.gb_Qa{border:none;color:#4285f4;cursor:default;font-weight:bold;outline:none;position:relative;text-align:center;text-decoration:none;text-transform:uppercase;white-space:nowrap;-webkit-user-select:none}a.gb_Qa:hover::after,a.gb_Qa:focus::after{background-color:rgba(0,0,0,.12);content:"";height:100%;left:0;position:absolute;top:0;width:100%}a.gb_Qa:hover,a.gb_Qa:focus{text-decoration:none}a.gb_Qa:active{background-color:rgba(153,153,153,.4);text-decoration:none}a.gb_Ra{background-color:#4285f4;color:#fff}a.gb_Ra:active{background-color:#0043b2}.gb_Sa{box-shadow:0 1px 1px rgba(0,0,0,.16)}.gb_Qa,.gb_Ra,.gb_Ta,.gb_Ua{display:inline-block;line-height:28px;padding:0 12px;border-radius:2px}.gb_Ta{background:#f8f8f8;border:1px solid #c6c6c6}.gb_Ua{background:#f8f8f8}.gb_Ta,#gb a.gb_Ta.gb_Ta,.gb_Ua{color:#666;cursor:default;text-decoration:none}#gb a.gb_Ua{cursor:default;text-decoration:none}.gb_Ua{border:1px solid #4285f4;font-weight:bold;outline:none;background:#4285f4;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#4387fd),to(#4683ea));background:-webkit-linear-gradient(top,#4387fd,#4683ea);background:linear-gradient(top,#4387fd,#4683ea);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#4387fd,endColorstr=#4683ea,GradientType=0)}#gb a.gb_Ua{color:#fff}.gb_Ua:hover{box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_Ua:active{box-shadow:inset 0 2px 0 rgba(0,0,0,.15);background:#3c78dc;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#3c7ae4),to(#3f76d3));background:-webkit-linear-gradient(top,#3c7ae4,#3f76d3);background:linear-gradient(top,#3c7ae4,#3f76d3);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#3c7ae4,endColorstr=#3f76d3,GradientType=0)}#gb .gb_Va{background:#fff;border:1px solid #dadce0;color:#1a73e8;display:inline-block;text-decoration:none}#gb .gb_Va:hover{background:#f8fbff;border-color:#dadce0;color:#174ea6}#gb .gb_Va:focus{background:#f4f8ff;color:#174ea6;outline:1px solid #174ea6}#gb .gb_Va:active,#gb .gb_Va:focus:active{background:#ecf3fe;color:#174ea6}#gb .gb_Va.gb_H{background:transparent;border:1px solid #5f6368;color:#8ab4f8;text-decoration:none}#gb .gb_Va.gb_H:hover{background:rgba(255,255,255,.04);color:#e8eaed}#gb .gb_Va.gb_H:focus{background:rgba(232,234,237,.12);color:#e8eaed;outline:1px solid #e8eaed}#gb .gb_Va.gb_H:active,#gb .gb_Va.gb_H:focus:active{background:rgba(232,234,237,.1);color:#e8eaed}.gb_dd{display:inline-block;vertical-align:middle}.gb_Oe .gb_Q{bottom:-3px;right:-5px}.gb_D{position:relative}.gb_B{display:inline-block;outline:none;vertical-align:middle;border-radius:2px;box-sizing:border-box;height:40px;width:40px;cursor:pointer;text-decoration:none}#gb#gb a.gb_B{cursor:pointer;text-decoration:none}.gb_B,a.gb_B{color:#000}.gb_ed{border-color:transparent;border-bottom-color:#fff;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;top:33px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s}.gb_fd{border-color:transparent;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-bottom-color:rgba(0,0,0,.2);top:32px}x:-o-prefocus,div.gb_fd{border-bottom-color:#ccc}.gb_la{background:#fff;border:1px solid #ccc;border-color:rgba(0,0,0,.2);color:#000;-webkit-box-shadow:0 2px 10px rgba(0,0,0,.2);box-shadow:0 2px 10px rgba(0,0,0,.2);display:none;outline:none;overflow:hidden;position:absolute;right:8px;top:62px;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-radius:2px;-webkit-user-select:text}.gb_dd.gb_Uc .gb_ed,.gb_dd.gb_Uc .gb_fd,.gb_dd.gb_Uc .gb_la,.gb_Uc.gb_la{display:block}.gb_dd.gb_Uc.gb_gd .gb_ed,.gb_dd.gb_Uc.gb_gd .gb_fd{display:none}.gb_Pe{position:absolute;right:8px;top:62px;z-index:-1}.gb_hd .gb_ed,.gb_hd .gb_fd,.gb_hd .gb_la{margin-top:-10px}.gb_dd:first-child,#gbsfw:first-child+.gb_dd{padding-left:4px}.gb_Fa.gb_Qe .gb_dd:first-child{padding-left:0}.gb_Re{position:relative}.gb_3c .gb_Re,.gb_Kd .gb_Re{float:right}.gb_B{padding:8px;cursor:pointer}.gb_B::after{content:"";position:absolute;top:-4px;bottom:-4px;left:-4px;right:-4px}.gb_Fa .gb_id:not(.gb_Qa):focus img{background-color:rgba(0,0,0,.2);outline:none;-webkit-border-radius:50%;border-radius:50%}.gb_jd button svg,.gb_B{-webkit-border-radius:50%;border-radius:50%}.gb_jd button:focus:not(:focus-visible) svg,.gb_jd button:hover svg,.gb_jd button:active svg,.gb_B:focus:not(:focus-visible),.gb_B:hover,.gb_B:active,.gb_B[aria-expanded=true]{outline:none}.gb_Mc .gb_jd.gb_kd button:focus-visible svg,.gb_jd button:focus-visible svg,.gb_B:focus-visible{outline:1px solid #202124}.gb_Mc .gb_jd button:focus-visible svg,.gb_Mc .gb_B:focus-visible{outline:1px solid #f1f3f4}@media (forced-colors:active){.gb_Mc .gb_jd.gb_kd button:focus-visible svg,.gb_jd button:focus-visible svg,.gb_Mc .gb_jd button:focus-visible svg{outline:1px solid currentcolor}}.gb_Mc .gb_jd.gb_kd button:focus svg,.gb_Mc .gb_jd.gb_kd button:focus:hover svg,.gb_jd button:focus svg,.gb_jd button:focus:hover svg,.gb_B:focus,.gb_B:focus:hover{background-color:rgba(60,64,67,.1)}.gb_Mc .gb_jd.gb_kd button:active svg,.gb_jd button:active svg,.gb_B:active{background-color:rgba(60,64,67,.12)}.gb_Mc .gb_jd.gb_kd button:hover svg,.gb_jd button:hover svg,.gb_B:hover{background-color:rgba(60,64,67,.08)}.gb_Wa .gb_B.gb_Za:hover{background-color:transparent}.gb_B[aria-expanded=true],.gb_B:hover[aria-expanded=true]{background-color:rgba(95,99,104,.24)}.gb_B[aria-expanded=true] .gb_F{fill:#5f6368;opacity:1}.gb_Mc .gb_jd button:hover svg,.gb_Mc .gb_B:hover{background-color:rgba(232,234,237,.08)}.gb_Mc .gb_jd button:focus svg,.gb_Mc .gb_jd button:focus:hover svg,.gb_Mc .gb_B:focus,.gb_Mc .gb_B:focus:hover{background-color:rgba(232,234,237,.1)}.gb_Mc .gb_jd button:active svg,.gb_Mc .gb_B:active{background-color:rgba(232,234,237,.12)}.gb_Mc .gb_B[aria-expanded=true],.gb_Mc .gb_B:hover[aria-expanded=true]{background-color:rgba(255,255,255,.12)}.gb_Mc .gb_B[aria-expanded=true] .gb_F{fill:#fff;opacity:1}.gb_dd{padding:4px}.gb_Fa.gb_Qe .gb_dd{padding:4px 2px}.gb_Fa.gb_Qe .gb_z.gb_dd{padding-left:6px}.gb_la{z-index:991;line-height:normal}.gb_la.gb_ld{left:0;right:auto}@media (max-width:350px){.gb_la.gb_ld{left:0}}.gb_Se .gb_la{top:56px}.gb_R{display:none!important}.gb_od{visibility:hidden}.gb_J .gb_B,.gb_ka .gb_J .gb_B{background-position:-64px -29px}.gb_1 .gb_J .gb_B{background-position:-29px -29px;opacity:1}.gb_J .gb_B,.gb_J .gb_B:hover,.gb_J .gb_B:focus{opacity:1}.gb_L{display:none}@media screen and (max-width:319px){.gb_md:not(.gb_nd) .gb_J{display:none;visibility:hidden}}.gb_Q{display:none}.gb_ad{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-size:20px;font-weight:400;letter-spacing:0.25px;line-height:48px;margin-bottom:2px;opacity:1;overflow:hidden;padding-left:16px;position:relative;text-overflow:ellipsis;vertical-align:middle;top:2px;white-space:nowrap;-webkit-flex:1 1 auto;-webkit-box-flex:1;flex:1 1 auto}.gb_ad.gb_bd{color:#3c4043}.gb_Fa.gb_cc .gb_ad{margin-bottom:0}.gb_td.gb_vd .gb_ad{padding-left:4px}.gb_Fa.gb_cc .gb_wd{position:relative;top:-2px}.gb_cd{display:none}.gb_Fa{color:black;min-width:160px;position:relative;-webkit-transition:box-shadow 250ms;transition:box-shadow 250ms}.gb_Fa.gb_Tc{min-width:120px}.gb_Fa.gb_xd .gb_yd{display:none}.gb_Fa.gb_xd .gb_md{height:56px}header.gb_Fa{display:block}.gb_Fa svg{fill:currentColor}.gb_Ed{position:fixed;top:0;width:100%}.gb_zd{-webkit-box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2);box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2)}.gb_Fd{height:64px}.gb_md{-webkit-box-sizing:border-box;box-sizing:border-box;position:relative;width:100%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:space-between;-webkit-justify-content:space-between;justify-content:space-between;min-width:-webkit-min-content;min-width:min-content}.gb_Fa:not(.gb_cc) .gb_md{padding:8px}.gb_Fa.gb_Hd .gb_md{-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_Fa .gb_md.gb_nd.gb_Id{min-width:0}.gb_Fa.gb_cc .gb_md{padding:4px;padding-left:8px;min-width:0}.gb_yd{height:48px;vertical-align:middle;white-space:nowrap;-webkit-box-align:center;-webkit-align-items:center;align-items:center;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-user-select:none}.gb_Bd>.gb_yd{display:table-cell;width:100%}.gb_td{padding-right:30px;box-sizing:border-box;-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_Fa.gb_cc .gb_td{padding-right:14px}.gb_Cd{-webkit-flex:1 1 100%;-webkit-box-flex:1;flex:1 1 100%}.gb_Cd>:only-child{display:inline-block}.gb_Dd.gb_4c{padding-left:4px}.gb_Dd.gb_Jd,.gb_Fa.gb_Hd .gb_Dd,.gb_Fa.gb_cc:not(.gb_Kd) .gb_Dd{padding-left:0}.gb_Fa.gb_cc .gb_Dd.gb_Jd{padding-right:0}.gb_Fa.gb_cc .gb_Dd.gb_Jd .gb_Wa{margin-left:10px}.gb_4c{display:inline}.gb_Fa.gb_Xc .gb_Dd.gb_Ld,.gb_Fa.gb_Kd .gb_Dd.gb_Ld{padding-left:2px}.gb_ad{display:inline-block}.gb_Dd{-webkit-box-sizing:border-box;box-sizing:border-box;height:48px;line-height:normal;padding:0 4px;padding-left:30px;-webkit-flex:0 0 auto;-webkit-box-flex:0;flex:0 0 auto;-webkit-box-pack:flex-end;-webkit-justify-content:flex-end;justify-content:flex-end}.gb_Kd{height:48px}.gb_Fa.gb_Kd{min-width:auto}.gb_Kd .gb_Dd{float:right;padding-left:32px}.gb_Kd .gb_Dd.gb_Md{padding-left:0}.gb_Nd{font-size:14px;max-width:200px;overflow:hidden;padding:0 12px;text-overflow:ellipsis;white-space:nowrap;-webkit-user-select:text}.gb_qd{-webkit-transition:background-color .4s;-webkit-transition:background-color .4s;transition:background-color .4s}.gb_Od{color:black}.gb_Mc{color:white}.gb_Fa a,.gb_Qc a{color:inherit}.gb_ba{color:rgba(0,0,0,.87)}.gb_Fa svg,.gb_Qc svg,.gb_td .gb_ud,.gb_3c .gb_ud{color:#5f6368;opacity:1}.gb_Mc svg,.gb_Qc.gb_Vc svg,.gb_Mc .gb_td .gb_ud,.gb_Mc .gb_td .gb_Lc,.gb_Mc .gb_td .gb_wd,.gb_Qc.gb_Vc .gb_ud{color:rgba(255,255,255,.87)}.gb_Mc .gb_td .gb_Pd:not(.gb_Qd){opacity:.87}.gb_bd{color:inherit;opacity:1;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased}.gb_Mc .gb_bd,.gb_Od .gb_bd{opacity:1}.gb_Rd{position:relative}.gb_M{font-family:arial,sans-serif;line-height:normal;padding-right:15px}a.gb_X,span.gb_X{color:rgba(0,0,0,.87);text-decoration:none}.gb_Mc a.gb_X,.gb_Mc span.gb_X{color:white}a.gb_X:focus{outline-offset:2px}a.gb_X:hover{text-decoration:underline}.gb_Z{display:inline-block;padding-left:15px}.gb_Z .gb_X{display:inline-block;line-height:24px;vertical-align:middle}.gb_rd{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-weight:500;font-size:14px;letter-spacing:.25px;line-height:16px;margin-left:10px;margin-right:8px;min-width:96px;padding:9px 23px;text-align:center;vertical-align:middle;border-radius:4px;box-sizing:border-box}.gb_Fa.gb_Kd .gb_rd{margin-left:8px}#gb a.gb_Ua.gb_rd{cursor:pointer}.gb_Ua.gb_rd:hover{background:#1b66c9;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ua.gb_rd:focus,.gb_Ua.gb_rd:hover:focus{background:#1c5fba;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ua.gb_rd:active{background:#1b63c1;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_rd{background:#1a73e8;border:1px solid transparent}.gb_Fa.gb_cc .gb_rd{padding:9px 15px;min-width:80px}.gb_Sd{text-align:left}#gb .gb_Mc a.gb_rd:not(.gb_H),#gb.gb_Mc a.gb_rd{background:#fff;border-color:#dadce0;-webkit-box-shadow:none;box-shadow:none;color:#1a73e8}#gb a.gb_Ua.gb_H.gb_rd{background:#8ab4f8;border:1px solid transparent;-webkit-box-shadow:none;box-shadow:none;color:#202124}#gb .gb_Mc a.gb_rd:hover:not(.gb_H),#gb.gb_Mc a.gb_rd:hover{background:#f8fbff;border-color:#cce0fc}#gb a.gb_Ua.gb_H.gb_rd:hover{background:#93baf9;border-color:transparent;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3)}#gb .gb_Mc a.gb_rd:focus:not(.gb_H),#gb .gb_Mc a.gb_rd:focus:hover:not(.gb_H),#gb.gb_Mc a.gb_rd:focus:not(.gb_H),#gb.gb_Mc a.gb_rd:focus:hover:not(.gb_H){background:#f4f8ff;outline:1px solid #c9ddfc}#gb a.gb_Ua.gb_H.gb_rd:focus,#gb a.gb_Ua.gb_H.gb_rd:focus:hover{background:#a6c6fa;border-color:transparent;-webkit-box-shadow:none;box-shadow:none}#gb .gb_Mc a.gb_rd:active:not(.gb_H),#gb.gb_Mc a.gb_rd:active{background:#ecf3fe}#gb a.gb_Ua.gb_H.gb_rd:active{background:#a1c3f9;-webkit-box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15);box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15)}.gb_K{display:none}@media screen and (max-width:319px){.gb_md .gb_J{display:none;visibility:hidden}}.gb_Wa{background-color:rgba(255,255,255,.88);border:1px solid #dadce0;-webkit-box-sizing:border-box;box-sizing:border-box;cursor:pointer;display:inline-block;max-height:48px;overflow:hidden;outline:none;padding:0;vertical-align:middle;width:134px;-webkit-border-radius:8px;border-radius:8px}.gb_Wa.gb_H{background-color:transparent;border:1px solid #5f6368}.gb_3a{display:inherit}.gb_Wa.gb_H .gb_3a{background:#fff;-webkit-border-radius:4px;border-radius:4px;display:inline-block;left:8px;margin-right:5px;position:relative;padding:3px;top:-1px}.gb_Wa:hover{border:1px solid #d2e3fc;background-color:rgba(248,250,255,.88)}.gb_Wa.gb_H:hover{background-color:rgba(241,243,244,.04);border:1px solid #5f6368}.gb_Wa:focus-visible,.gb_Wa:focus{background-color:#fff;outline:1px solid #202124;-webkit-box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15);box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15)}.gb_Wa.gb_H:focus-visible,.gb_Wa.gb_H:focus{background-color:rgba(241,243,244,.12);outline:1px solid #f1f3f4;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3)}.gb_Wa.gb_H:active,.gb_Wa.gb_Uc.gb_H:focus{background-color:rgba(241,243,244,.1);border:1px solid #5f6368}.gb_4a{display:inline-block;padding-bottom:2px;padding-left:7px;padding-top:2px;text-align:center;vertical-align:middle;line-height:32px;width:78px}.gb_Wa.gb_H .gb_4a{line-height:26px;margin-left:0;padding-bottom:0;padding-left:0;padding-top:0;width:72px}.gb_4a.gb_5a{background-color:#f1f3f4;-webkit-border-radius:4px;border-radius:4px;margin-left:8px;padding-left:0;line-height:30px}.gb_4a.gb_5a .gb_Jc{vertical-align:middle}.gb_Fa:not(.gb_cc) .gb_Wa{margin-left:10px;margin-right:4px}.gb_Td{max-height:32px;width:78px}.gb_Wa.gb_H .gb_Td{max-height:26px;width:72px}.gb_P{-webkit-background-size:32px 32px;background-size:32px 32px;border:0;-webkit-border-radius:50%;border-radius:50%;display:block;margin:0px;position:relative;height:32px;width:32px;z-index:0}.gb_eb{background-color:#e8f0fe;border:1px solid rgba(32,33,36,.08);position:relative}.gb_eb.gb_P{height:30px;width:30px}.gb_eb.gb_P:hover,.gb_eb.gb_P:active{-webkit-box-shadow:none;box-shadow:none}.gb_fb{background:#fff;border:none;-webkit-border-radius:50%;border-radius:50%;bottom:2px;-webkit-box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);height:14px;margin:2px;position:absolute;right:0;width:14px}.gb_wc{color:#1f71e7;font:400 22px/32px Google Sans,Roboto,Helvetica,Arial,sans-serif;text-align:center;text-transform:uppercase}@media (-webkit-min-device-pixel-ratio:1.25),(min-resolution:1.25dppx),(min-device-pixel-ratio:1.25){.gb_P::before,.gb_gb::before{display:inline-block;-webkit-transform:scale(0.5);-webkit-transform:scale(0.5);transform:scale(0.5);-webkit-transform-origin:left 0;-webkit-transform-origin:left 0;transform-origin:left 0}.gb_3 .gb_gb::before{-webkit-transform:scale(scale(0.416666667));-webkit-transform:scale(scale(0.416666667));transform:scale(scale(0.416666667))}}.gb_P:hover,.gb_P:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_P:active{-webkit-box-shadow:inset 0 2px 0 rgba(0,0,0,.15);box-shadow:inset 0 2px 0 rgba(0,0,0,.15)}.gb_P:active::after{background:rgba(0,0,0,.1);-webkit-border-radius:50%;border-radius:50%;content:"";display:block;height:100%}.gb_hb{cursor:pointer;line-height:40px;min-width:30px;opacity:.75;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}.gb_B.gb_hb{width:auto}.gb_hb:hover,.gb_hb:focus{opacity:.85}.gb_hd .gb_hb,.gb_hd .gb_Vd{line-height:26px}#gb#gb.gb_hd a.gb_hb,.gb_hd .gb_Vd{font-size:11px;height:auto}.gb_ib{border-top:4px solid #000;border-left:4px dashed transparent;border-right:4px dashed transparent;display:inline-block;margin-left:6px;opacity:.75;vertical-align:middle}.gb_Za:hover .gb_ib{opacity:.85}.gb_Wa>.gb_z{padding:3px 3px 3px 4px}.gb_Wd.gb_od{color:#fff}.gb_1 .gb_hb,.gb_1 .gb_ib{opacity:1}#gb#gb.gb_1.gb_1 a.gb_hb,#gb#gb .gb_1.gb_1 a.gb_hb{color:#fff}.gb_1.gb_1 .gb_ib{border-top-color:#fff;opacity:1}.gb_ka .gb_P:hover,.gb_1 .gb_P:hover,.gb_ka .gb_P:focus,.gb_1 .gb_P:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2);box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2)}.gb_Xd .gb_z,.gb_Zd .gb_z{position:absolute;right:1px}.gb_z.gb_0,.gb_jb.gb_0,.gb_Za.gb_0{-webkit-flex:0 1 auto;-webkit-box-flex:0;flex:0 1 auto}.gb_0d.gb_1d .gb_hb{width:30px!important}.gb_2d{height:40px;position:absolute;right:-5px;top:-5px;width:40px}.gb_3d .gb_2d,.gb_4d .gb_2d{right:0;top:0}.gb_z .gb_B{padding:4px}.gb_S{display:none}sentinel{}</style><script nonce="">;this.gbar_={CONFIG:[[[0,"www.gstatic.com","og.qtm.en_US.5MDp2wjsNx8.2019.O","com.bd","en","425",0,[4,2,"","","","768919215","0"],null,"AeNPaOy0KuXOp84PzOPQkQM",null,0,"og.qtm.iKf-j4fvYQ4.L.W.O","AA2YrTv8f8ZUbipJWUaxHHl3oxLPlmHPDA","AA2YrTsKeM0fuGSyAulS_7nCvnwvUw1LAA","",2,1,200,"BGD",null,null,"425","425",1,null,null,114591953,null,0,0],null,[1,0.1000000014901161,2,1],null,[1,0,1,null,"0","u2004095@student.cuet.ac.bd","","AIhRldKtHrQlUBXIAIrn5ulbXDnmMY3udAS6A8DCu76NxD0JnwuZzQ457ngP6hGauoGrDN30M4MNngljbAyBRn6VqTeoCH5jq_YzvUI0sgTPQFbsLUOuHW8",0,0,0,""],[0,0,"",1,0,0,0,0,0,0,null,0,0,null,0,0,null,null,0,0,0,"","","","","","",null,0,0,0,0,0,null,null,null,"rgba(32,33,36,1)","rgba(255,255,255,1)",0,0,0,null,null,null,0],["%1$s (default)","Brand account",1,"%1$s (delegated)",1,null,83,"https://colab.research.google.com/?authuser=$authuser",null,null,null,1,"https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en\u0026ts=250",0,"dashboard",null,null,null,null,"Profile","",1,null,"Signed out","https://accounts.google.com/AccountChooser?source=ogb\u0026continue=$continue\u0026Email=$email\u0026ec=GAhAqQM","https://accounts.google.com/RemoveLocalAccount?source=ogb","Remove","Sign in",0,1,1,0,1,1,0,null,null,null,"Session expired",null,null,null,"Visitor",null,"Default","Delegated","Sign out of all accounts",1,null,null,0,null,null,"myaccount.google.com","https",0,1,0],null,["1","gci_91f30755d6a6b787dcc2a4062e6e9824.js","googleapis.client:gapi.iframes","0","en"],null,null,null,null,["m;/_/scs/abc-static/_/js/k=gapi.gapi.en.citSWp3NP7U.O/d=1/rs=AHpOoo9xL6HUJcSIDSbTUlNBOsamhv5RMA/m=__features__","https://apis.google.com","","","1","",null,1,"es_plusone_gc_20250505.0_p1","en",null,0],[0.009999999776482582,"com.bd","425",[null,"","0",null,1,5184000,null,null,"",null,null,null,null,null,0,null,0,null,1,0,0,0,null,null,0,0,null,0,0,0,0,0],null,null,null,0],[1,null,null,40400,425,"BGD","en","768919215.0",8,null,1,0,null,null,null,null,"103054292,103054294,103133349,103133351,103247483,103247486",null,null,null,"AeNPaOy0KuXOp84PzOPQkQM",0,0,0,null,2,5,"nn",69,0,0,0,0,1,114591953,0,0],[[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.5MDp2wjsNx8.2019.O/rt=j/m=qabr,qgl,q_dnp,qcwid,qbd,qapid,qads,qrcd,q_dg/exm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/rs=AA2YrTv8f8ZUbipJWUaxHHl3oxLPlmHPDA"],[null,null,null,"https://www.gstatic.com/og/_/ss/k=og.qtm.iKf-j4fvYQ4.L.W.O/m=qcwid,qba/excm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/ct=zgms/rs=AA2YrTsKeM0fuGSyAulS_7nCvnwvUw1LAA"]],null,null,null,[[[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/account?yac=1\u0026bac=1\u0026amb=1\u0026acsl=1\u0026gdafe=1"],0,414,436,57,4,1,0,0,65,66,8000,"https://accounts.google.com/SignOutOptions?hl=en\u0026continue=https://colab.research.google.com/\u0026ec=GBRAqQM",68,2,null,null,1,113,"Something went wrong.%1$s Refresh to try again or %2$schoose another account%3$s.",3,null,null,75,0,null,null,null,null,null,null,null,"/widget/account",["https","myaccount.google.com",0,32,83,0],0,0,1,["Critical security alert","Important account alert","Storage usage alert",1,1],0,1,null,1,1,1,1,null,null,0,0,0,null,0,0],[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/callout/sid?dc=1"],null,280,420,70,25,0,null,0,null,null,8000,null,71,4,null,null,null,null,null,null,null,null,76,null,null,null,107,108,109,"",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0]],null,null,"425","425",1,0,null,"en",0,["https://colab.research.google.com/?authuser=$authuser","https://accounts.google.com/AddSession?hl=en\u0026continue=https://colab.research.google.com/\u0026ec=GAlAqQM","https://accounts.google.com/Logout?hl=en\u0026continue=https://colab.research.google.com/\u0026timeStmp=1750065921\u0026secTok=.AG5fkS8P7nT9FkTcQlJTyHc4QsOrweHQRA\u0026ec=GAdAqQM","https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en\u0026ts=250",0,0,"",0,0,null,0,0,"https://accounts.google.com/ServiceLogin?passive=true\u0026continue=https%3A%2F%2Fcolab.research.google.com%2F\u0026ec=GAZAqQM",1,1,0,0,null,0],0,0,0,[null,"",null,null,null,1,null,0,0,"","","","https://ogads-pa.clients6.google.com",0,0,0,"","",0,0,null,86400,null,1,1,null,0,null,0,0,"8559284470",0,0],0,null,null,null,1,0,"u2004095@student.cuet.ac.bd"],null,[["mousedown","touchstart","touchmove","wheel","keydown"],300000],[[null,null,null,"https://accounts.google.com/RotateCookiesPage"],3,null,null,null,0,1]]],};this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_._F_toggles_initialize=function(a){(typeof globalThis!=="undefined"?globalThis:typeof self!=="undefined"?self:this)._F_toggles=a||[]};(0,_._F_toggles_initialize)([]);
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var ja,pa,qa,ua,wa,xa,Ga,Ha,ab,db,fb,kb,gb,lb,rb,Fb,Gb,Hb,Ib;_.aa=function(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,_.aa);else{const c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));b!==void 0&&(this.cause=b)};_.ba=function(a){a.Qj=!0;return a};_.ia=function(a){var b=a;if(da(b)){if(!/^\s*(?:-?[1-9]\d*|0)?\s*$/.test(b))throw Error(String(b));}else if(ea(b)&&!Number.isSafeInteger(b))throw Error(String(b));return fa?BigInt(a):a=ha(a)?a?"1":"0":da(a)?a.trim()||"0":String(a)};
ja=function(a,b){if(a.length>b.length)return!1;if(a.length<b.length||a===b)return!0;for(let c=0;c<a.length;c++){const d=a[c],e=b[c];if(d>e)return!1;if(d<e)return!0}};_.ka=function(a){_.t.setTimeout(()=>{throw a;},0)};_.ma=function(){return _.la().toLowerCase().indexOf("webkit")!=-1};_.la=function(){var a=_.t.navigator;return a&&(a=a.userAgent)?a:""};pa=function(a){if(!na||!oa)return!1;for(let b=0;b<oa.brands.length;b++){const {brand:c}=oa.brands[b];if(c&&c.indexOf(a)!=-1)return!0}return!1};
_.u=function(a){return _.la().indexOf(a)!=-1};qa=function(){return na?!!oa&&oa.brands.length>0:!1};_.ra=function(){return qa()?!1:_.u("Opera")};_.sa=function(){return qa()?!1:_.u("Trident")||_.u("MSIE")};_.ta=function(){return _.u("Firefox")||_.u("FxiOS")};_.va=function(){return _.u("Safari")&&!(ua()||(qa()?0:_.u("Coast"))||_.ra()||(qa()?0:_.u("Edge"))||(qa()?pa("Microsoft Edge"):_.u("Edg/"))||(qa()?pa("Opera"):_.u("OPR"))||_.ta()||_.u("Silk")||_.u("Android"))};
ua=function(){return qa()?pa("Chromium"):(_.u("Chrome")||_.u("CriOS"))&&!(qa()?0:_.u("Edge"))||_.u("Silk")};wa=function(){return na?!!oa&&!!oa.platform:!1};xa=function(){return _.u("iPhone")&&!_.u("iPod")&&!_.u("iPad")};_.ya=function(){return xa()||_.u("iPad")||_.u("iPod")};_.za=function(){return wa()?oa.platform==="macOS":_.u("Macintosh")};_.Ba=function(a,b){return _.Aa(a,b)>=0};_.Ca=function(a,b=!1){return b&&Symbol.for&&a?Symbol.for(a):a!=null?Symbol(a):Symbol()};
_.Da=function(a){if(4&a)return 512&a?512:1024&a?1024:0};_.Fa=function(a,b){return b===void 0?a.i!==Ea&&!!(2&(a.ha[_.v]|0)):!!(2&b)&&a.i!==Ea};Ga=function(a){return a};Ha=function(a,b){a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity=b};_.Ia=function(a){a=Error(a);Ha(a,"warning");return a};_.Ka=function(a,b){if(a!=null){var c;var d=(c=Ja)!=null?c:Ja={};c=d[a]||0;c>=b||(d[a]=c+1,a=Error(),Ha(a,"incident"),_.ka(a))}};
_.Ma=function(a){if(typeof a!=="boolean")throw Error("r`"+_.La(a)+"`"+a);return a};_.Na=function(a){if(a==null||typeof a==="boolean")return a;if(typeof a==="number")return!!a};_.Pa=function(a){if(!(0,_.Oa)(a))throw _.Ia("enum");return a|0};_.Qa=function(a){return a==null?a:(0,_.Oa)(a)?a|0:void 0};_.Ra=function(a){if(typeof a!=="number")throw _.Ia("int32");if(!(0,_.Oa)(a))throw _.Ia("int32");return a|0};_.Sa=function(a){if(a!=null&&typeof a!=="string")throw Error();return a};
_.Ta=function(a){return a==null||typeof a==="string"?a:void 0};_.Wa=function(a,b,c){if(a!=null&&a[_.Ua]===_.Va)return a;if(Array.isArray(a)){var d=a[_.v]|0;c=d|c&32|c&2;c!==d&&(a[_.v]=c);return new b(a)}};_.Za=function(a){const b=_.Xa(_.Ya);return b?a[b]:void 0};ab=function(a,b){b<100||_.Ka($a,1)};
db=function(a,b,c,d){const e=d!==void 0;d=!!d;var f=_.Xa(_.Ya),g;!e&&f&&(g=a[f])&&g.qd(ab);f=[];var h=a.length;let k;g=4294967295;let l=!1;const m=!!(b&64),p=m?b&128?0:-1:void 0;if(!(b&1||(k=h&&a[h-1],k!=null&&typeof k==="object"&&k.constructor===Object?(h--,g=h):k=void 0,!m||b&128||e))){l=!0;var r;g=((r=bb)!=null?r:Ga)(g-p,p,a,k)+p}b=void 0;for(r=0;r<h;r++){let w=a[r];if(w!=null&&(w=c(w,d))!=null)if(m&&r>=g){const E=r-p;var q=void 0;((q=b)!=null?q:b={})[E]=w}else f[r]=w}if(k)for(let w in k){q=k[w];
if(q==null||(q=c(q,d))==null)continue;h=+w;let E;if(m&&!Number.isNaN(h)&&(E=h+p)<g)f[E]=q;else{let K;((K=b)!=null?K:b={})[w]=q}}b&&(l?f.push(b):f[g]=b);e&&_.Xa(_.Ya)&&(a=_.Za(a))&&"function"==typeof _.cb&&a instanceof _.cb&&(f[_.Ya]=a.i());return f};
fb=function(a){switch(typeof a){case "number":return Number.isFinite(a)?a:""+a;case "bigint":return(0,_.eb)(a)?Number(a):""+a;case "boolean":return a?1:0;case "object":if(Array.isArray(a)){const b=a[_.v]|0;return a.length===0&&b&1?void 0:db(a,b,fb)}if(a!=null&&a[_.Ua]===_.Va)return gb(a);if("function"==typeof _.hb&&a instanceof _.hb)return a.j();return}return a};kb=function(a,b){if(b){bb=b==null||b===Ga||b[ib]!==jb?Ga:b;try{return gb(a)}finally{bb=void 0}}return gb(a)};
gb=function(a){a=a.ha;return db(a,a[_.v]|0,fb)};
_.mb=function(a,b,c,d=0){if(a==null){var e=32;c?(a=[c],e|=128):a=[];b&&(e=e&-8380417|(b&1023)<<13)}else{if(!Array.isArray(a))throw Error("s");e=a[_.v]|0;2048&e&&!(2&e)&&lb();if(e&256)throw Error("u");if(e&64)return d!==0||e&2048||(a[_.v]=e|2048),a;if(c&&(e|=128,c!==a[0]))throw Error("v");a:{c=a;e|=64;var f=c.length;if(f){var g=f-1;const k=c[g];if(k!=null&&typeof k==="object"&&k.constructor===Object){b=e&128?0:-1;g-=b;if(g>=1024)throw Error("x");for(var h in k)if(f=+h,f<g)c[f+b]=k[h],delete k[h];else break;
e=e&-8380417|(g&1023)<<13;break a}}if(b){h=Math.max(b,f-(e&128?0:-1));if(h>1024)throw Error("y");e=e&-8380417|(h&1023)<<13}}}e|=64;d===0&&(e|=2048);a[_.v]=e;return a};lb=function(){_.Ka(nb,5)};
rb=function(a,b){if(typeof a!=="object")return a;if(Array.isArray(a)){var c=a[_.v]|0;a.length===0&&c&1?a=void 0:c&2||(!b||4096&c||16&c?a=_.ob(a,c,!1,b&&!(c&16)):(a[_.v]|=34,c&4&&Object.freeze(a)));return a}if(a!=null&&a[_.Ua]===_.Va)return b=a.ha,c=b[_.v]|0,_.Fa(a,c)?a:_.pb(a,b,c)?_.qb(a,b):_.ob(b,c);if("function"==typeof _.hb&&a instanceof _.hb)return a};_.qb=function(a,b,c){a=new a.constructor(b);c&&(a.i=Ea);a.o=Ea;return a};
_.ob=function(a,b,c,d){d!=null||(d=!!(34&b));a=db(a,b,rb,d);d=32;c&&(d|=2);b=b&8380609|d;a[_.v]=b;return a};_.tb=function(a){const b=a.ha,c=b[_.v]|0;return _.Fa(a,c)?_.pb(a,b,c)?_.qb(a,b,!0):new a.constructor(_.ob(b,c,!1)):a};_.ub=function(a){if(a.i!==Ea)return!1;var b=a.ha;b=_.ob(b,b[_.v]|0);b[_.v]|=2048;a.ha=b;a.i=void 0;a.o=void 0;return!0};_.vb=function(a){if(!_.ub(a)&&_.Fa(a,a.ha[_.v]|0))throw Error();};_.wb=function(a,b){b===void 0&&(b=a[_.v]|0);b&32&&!(b&4096)&&(a[_.v]=b|4096)};
_.pb=function(a,b,c){return c&2?!0:c&32&&!(c&4096)?(b[_.v]=c|2,a.i=Ea,!0):!1};_.xb=function(a,b,c,d,e){const f=c+(e?0:-1);var g=a.length-1;if(g>=1+(e?0:-1)&&f>=g){const h=a[g];if(h!=null&&typeof h==="object"&&h.constructor===Object)return h[c]=d,b}if(f<=g)return a[f]=d,b;if(d!==void 0){let h;g=((h=b)!=null?h:b=a[_.v]|0)>>13&1023||536870912;c>=g?d!=null&&(a[g+(e?0:-1)]={[c]:d}):a[f]=d}return b};_.yb=function(a){return!!(2&a)&&!!(4&a)||!!(256&a)};
_.Ab=function(a,b,c,d,e){let f=!1;d=_.zb(a,d,e,g=>{const h=_.Wa(g,c,b);f=h!==g&&h!=null;return h});if(d!=null)return f&&!_.Fa(d)&&_.wb(a,b),d};_.Bb=function(a,b){return a=(2&b?a|2:a&-3)&-273};_.Cb=function(){const a=class{constructor(){throw Error();}};Object.setPrototypeOf(a,a.prototype);return a};_.x=function(a,b){return a!=null?!!a:!!b};_.y=function(a,b){b==void 0&&(b="");return a!=null?a:b};_.Db=function(a,b,c){for(const d in a)b.call(c,a[d],d,a)};_.Eb=function(a){for(const b in a)return!1;return!0};
Fb=Object.defineProperty;Gb=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("a");};Hb=Gb(this);Ib=function(a,b){if(b)a:{var c=Hb;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&b!=null&&Fb(c,a,{configurable:!0,writable:!0,value:b})}};
Ib("globalThis",function(a){return a||Hb});Ib("Symbol.dispose",function(a){return a?a:Symbol("b")});Ib("Promise.prototype.finally",function(a){return a?a:function(b){return this.then(function(c){return Promise.resolve(b()).then(function(){return c})},function(c){return Promise.resolve(b()).then(function(){throw c;})})}});
Ib("Array.prototype.flat",function(a){return a?a:function(b){b=b===void 0?1:b;var c=[];Array.prototype.forEach.call(this,function(d){Array.isArray(d)&&b>0?(d=Array.prototype.flat.call(d,b-1),c.push.apply(c,d)):c.push(d)});return c}});var Kb,Ob;_.Jb=_.Jb||{};_.t=this||self;Kb=_.t._F_toggles||[];_.Lb=function(a,b){a=a.split(".");b=b||_.t;for(var c=0;c<a.length;c++)if(b=b[a[c]],b==null)return null;return b};_.La=function(a){var b=typeof a;return b!="object"?b:a?Array.isArray(a)?"array":b:"null"};_.Mb=function(a){var b=typeof a;return b=="object"&&a!=null||b=="function"};_.Nb="closure_uid_"+(Math.random()*1E9>>>0);Ob=function(a,b,c){return a.call.apply(a.bind,arguments)};_.z=function(a,b,c){_.z=Ob;return _.z.apply(null,arguments)};
_.Pb=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}};_.A=function(a,b){a=a.split(".");for(var c=_.t,d;a.length&&(d=a.shift());)a.length||b===void 0?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b};_.Xa=function(a){return a};
_.B=function(a,b){function c(){}c.prototype=b.prototype;a.X=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.Ij=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}};_.B(_.aa,Error);_.aa.prototype.name="CustomError";var ea=_.ba(a=>typeof a==="number"),da=_.ba(a=>typeof a==="string"),ha=_.ba(a=>typeof a==="boolean");var fa=typeof _.t.BigInt==="function"&&typeof _.t.BigInt(0)==="bigint";var Sb,Qb,Tb,Rb;_.eb=_.ba(a=>fa?a>=Qb&&a<=Rb:a[0]==="-"?ja(a,Sb):ja(a,Tb));Sb=Number.MIN_SAFE_INTEGER.toString();Qb=fa?BigInt(Number.MIN_SAFE_INTEGER):void 0;Tb=Number.MAX_SAFE_INTEGER.toString();Rb=fa?BigInt(Number.MAX_SAFE_INTEGER):void 0;_.Ub=typeof TextDecoder!=="undefined";_.Vb=typeof TextEncoder!=="undefined";var Wb=!!(Kb[0]>>16&1);var Xb;if(Kb[0]>>15&1)Xb=Wb;else{var Yb=_.Lb("WIZ_global_data.oxN3nb"),Zb=Yb&&Yb[610401301];Xb=Zb!=null?Zb:!1}var na=Xb;var oa,$b=_.t.navigator;oa=$b?$b.userAgentData||null:null;_.Aa=function(a,b){return Array.prototype.indexOf.call(a,b,void 0)};_.ac=function(a,b,c){Array.prototype.forEach.call(a,b,c)};_.bc=function(a,b){return Array.prototype.some.call(a,b,void 0)};_.cc=function(a){_.cc[" "](a);return a};_.cc[" "]=function(){};var qc;_.dc=_.ra();_.ec=_.sa();_.fc=_.u("Edge");_.hc=_.u("Gecko")&&!(_.ma()&&!_.u("Edge"))&&!(_.u("Trident")||_.u("MSIE"))&&!_.u("Edge");_.ic=_.ma()&&!_.u("Edge");_.jc=_.za();_.kc=wa()?oa.platform==="Windows":_.u("Windows");_.lc=wa()?oa.platform==="Android":_.u("Android");_.mc=xa();_.nc=_.u("iPad");_.oc=_.u("iPod");_.pc=_.ya();
a:{let a="";const b=function(){const c=_.la();if(_.hc)return/rv:([^\);]+)(\)|;)/.exec(c);if(_.fc)return/Edge\/([\d\.]+)/.exec(c);if(_.ec)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(c);if(_.ic)return/WebKit\/(\S+)/.exec(c);if(_.dc)return/(?:Version)[ \/]?(\S+)/.exec(c)}();b&&(a=b?b[1]:"");if(_.ec){var rc;const c=_.t.document;rc=c?c.documentMode:void 0;if(rc!=null&&rc>parseFloat(a)){qc=String(rc);break a}}qc=a}_.sc=qc;_.tc=_.ta();_.uc=xa()||_.u("iPod");_.vc=_.u("iPad");_.wc=_.u("Android")&&!(ua()||_.ta()||_.ra()||_.u("Silk"));_.xc=ua();_.yc=_.va()&&!_.ya();var $a,nb,ib;_.Ya=_.Ca();_.zc=_.Ca();$a=_.Ca();_.Ac=_.Ca();nb=_.Ca();_.Ua=_.Ca("m_m",!0);ib=_.Ca();_.Bc=_.Ca();var Dc;_.v=_.Ca("jas",!0);Dc=[];Dc[_.v]=7;_.Cc=Object.freeze(Dc);var Ea;_.Va={};Ea={};_.Ec=Object.freeze({});var jb={};var Ja=void 0;_.Fc=typeof BigInt==="function"?BigInt.asIntN:void 0;_.Gc=Number.isSafeInteger;_.Oa=Number.isFinite;_.Hc=Math.trunc;var bb;_.Ic=_.ia(0);_.Jc={};_.Kc=function(a,b,c,d,e){b=_.zb(a.ha,b,c,e);if(b!==null||d&&a.o!==Ea)return b};_.zb=function(a,b,c,d){if(b===-1)return null;const e=b+(c?0:-1),f=a.length-1;let g,h;if(!(f<1+(c?0:-1))){if(e>=f)if(g=a[f],g!=null&&typeof g==="object"&&g.constructor===Object)c=g[b],h=!0;else if(e===f)c=g;else return;else c=a[e];if(d&&c!=null){d=d(c);if(d==null)return d;if(!Object.is(d,c))return h?g[b]=d:a[e]=d,d}return c}};_.Lc=function(a,b,c,d){_.vb(a);const e=a.ha;_.xb(e,e[_.v]|0,b,c,d);return a};
_.C=function(a,b,c,d){let e=a.ha,f=e[_.v]|0;b=_.Ab(e,f,b,c,d);if(b==null)return b;f=e[_.v]|0;if(!_.Fa(a,f)){const g=_.tb(b);g!==b&&(_.ub(a)&&(e=a.ha,f=e[_.v]|0),b=g,f=_.xb(e,f,c,b,d),_.wb(e,f))}return b};_.D=function(a,b,c){c==null&&(c=void 0);_.Lc(a,b,c);c&&!_.Fa(c)&&_.wb(a.ha);return a};_.Nc=function(a,b,c,d){return _.Qa(_.Kc(a,b,c,d))};_.F=function(a,b,c=!1,d){let e;return(e=_.Na(_.Kc(a,b,d)))!=null?e:c};_.G=function(a,b,c="",d){let e;return(e=_.Ta(_.Kc(a,b,d)))!=null?e:c};
_.H=function(a,b,c){return _.Ta(_.Kc(a,b,c,_.Jc))};_.J=function(a,b,c,d){return _.Lc(a,b,c==null?c:_.Ma(c),d)};_.L=function(a,b,c){return _.Lc(a,b,c==null?c:_.Ra(c))};_.M=function(a,b,c,d){return _.Lc(a,b,_.Sa(c),d)};_.N=function(a,b,c,d){return _.Lc(a,b,c==null?c:_.Pa(c),d)};_.O=class{constructor(a,b,c){this.ha=_.mb(a,b,c)}toJSON(){return kb(this)}va(a){return JSON.stringify(kb(this,a))}};_.O.prototype[_.Ua]=_.Va;_.O.prototype.toString=function(){return this.ha.toString()};_.Oc=_.Cb();_.Pc=_.Cb();_.Qc=_.Cb();_.Rc=Symbol();var Sc=class extends _.O{constructor(a){super(a)}};_.Tc=class extends _.O{constructor(a){super(a)}D(a){return _.L(this,3,a)}};var Uc=class extends _.O{constructor(a){super(a)}Hc(a){return _.M(this,24,a)}};_.Vc=class extends _.O{constructor(a){super(a)}};_.Q=function(){this.qa=this.qa;this.Y=this.Y};_.Q.prototype.qa=!1;_.Q.prototype.isDisposed=function(){return this.qa};_.Q.prototype.dispose=function(){this.qa||(this.qa=!0,this.R())};_.Q.prototype[Symbol.dispose]=function(){this.dispose()};_.Q.prototype.R=function(){if(this.Y)for(;this.Y.length;)this.Y.shift()()};var Wc=class extends _.Q{constructor(){var a=window;super();this.o=a;this.i=[];this.j={}}resolve(a){let b=this.o;a=a.split(".");const c=a.length;for(let d=0;d<c;++d)if(b[a[d]])b=b[a[d]];else return null;return b instanceof Function?b:null}ob(){const a=this.i.length,b=this.i,c=[];for(let d=0;d<a;++d){const e=b[d].i(),f=this.resolve(e);if(f&&f!=this.j[e])try{b[d].ob(f)}catch(g){}else c.push(b[d])}this.i=c.concat(b.slice(a))}};var Yc=class extends _.Q{constructor(){var a=_.Xc;super();this.o=a;this.A=this.i=null;this.v=0;this.B={};this.j=!1;a=window.navigator.userAgent;a.indexOf("MSIE")>=0&&a.indexOf("Trident")>=0&&(a=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a))&&a[1]&&parseFloat(a[1])<9&&(this.j=!0)}C(a,b){this.i=b;this.A=a;b.preventDefault?b.preventDefault():b.returnValue=!1}};_.Zc=class extends _.O{constructor(a){super(a)}};var $c=class extends _.O{constructor(a){super(a)}};var cd;_.ad=function(a,b,c=98,d=new _.Tc){if(a.i){const e=new Sc;_.M(e,1,b.message);_.M(e,2,b.stack);_.L(e,3,b.lineNumber);_.N(e,5,1);_.D(d,40,e);a.i.log(c,d)}};cd=class{constructor(){var a=bd;this.i=null;_.F(a,4,!0)}log(a,b,c=new _.Tc){_.ad(this,a,98,c)}};var dd,ed;dd=function(a){if(a.o.length>0){var b=a.i!==void 0,c=a.j!==void 0;if(b||c){b=b?a.v:a.A;c=a.o;a.o=[];try{_.ac(c,b,a)}catch(d){console.error(d)}}}};_.fd=class{constructor(a){this.i=a;this.j=void 0;this.o=[]}then(a,b,c){this.o.push(new ed(a,b,c));dd(this)}resolve(a){if(this.i!==void 0||this.j!==void 0)throw Error("C");this.i=a;dd(this)}reject(a){if(this.i!==void 0||this.j!==void 0)throw Error("C");this.j=a;dd(this)}v(a){a.j&&a.j.call(a.i,this.i)}A(a){a.o&&a.o.call(a.i,this.j)}};
ed=class{constructor(a,b,c){this.j=a;this.o=b;this.i=c}};_.gd=a=>{var b="lc";if(a.lc&&a.hasOwnProperty(b))return a.lc;b=new a;return a.lc=b};_.hd=class{constructor(){this.v=new _.fd;this.i=new _.fd;this.D=new _.fd;this.B=new _.fd;this.C=new _.fd;this.A=new _.fd;this.o=new _.fd;this.j=new _.fd;this.F=new _.fd}Y(){return this.v}M(){return this.i}N(){return this.D}L(){return this.B}qa(){return this.C}K(){return this.A}J(){return this.o}G(){return this.j}static i(){return _.gd(_.hd)}};var ld;_.jd=function(){return _.C(_.id,Uc,1)};_.kd=function(){return _.C(_.id,_.Vc,5)};ld=class extends _.O{constructor(a){super(a)}};var md;window.gbar_&&window.gbar_.CONFIG?md=window.gbar_.CONFIG[0]||{}:md=[];_.id=new ld(md);var bd=_.C(_.id,$c,3)||new $c;_.jd()||new Uc;_.Xc=new cd;_.A("gbar_._DumpException",function(a){_.Xc?_.Xc.log(a):console.error(a)});_.nd=new Yc;var pd;_.qd=function(a,b){var c=_.od.i();if(a in c.i){if(c.i[a]!=b)throw new pd;}else{c.i[a]=b;const h=c.j[a];if(h)for(let k=0,l=h.length;k<l;k++){b=h[k];var d=c.i;delete b.i[a];if(_.Eb(b.i)){for(var e=b.j.length,f=Array(e),g=0;g<e;g++)f[g]=d[b.j[g]];b.o.apply(b.v,f)}}delete c.j[a]}};_.od=class{constructor(){this.i={};this.j={}}static i(){return _.gd(_.od)}};_.rd=class extends _.aa{constructor(){super()}};pd=class extends _.rd{};_.A("gbar.A",_.fd);_.fd.prototype.aa=_.fd.prototype.then;_.A("gbar.B",_.hd);_.hd.prototype.ba=_.hd.prototype.M;_.hd.prototype.bb=_.hd.prototype.N;_.hd.prototype.bd=_.hd.prototype.qa;_.hd.prototype.bf=_.hd.prototype.Y;_.hd.prototype.bg=_.hd.prototype.L;_.hd.prototype.bh=_.hd.prototype.K;_.hd.prototype.bj=_.hd.prototype.J;_.hd.prototype.bk=_.hd.prototype.G;_.A("gbar.a",_.hd.i());window.gbar&&window.gbar.ap&&window.gbar.ap(window.gbar.a);var sd=new Wc;_.qd("api",sd);
var td=_.kd()||new _.Vc,ud=window,vd=_.y(_.H(td,8));ud.__PVT=vd;_.qd("eq",_.nd);
}catch(e){_._DumpException(e)}
try{
_.wd=class extends _.O{constructor(a){super(a)}};
}catch(e){_._DumpException(e)}
try{
var xd=class extends _.O{constructor(a){super(a)}};var yd=class extends _.Q{constructor(){super();this.j=[];this.i=[]}o(a,b){this.j.push({features:a,options:b!=null?b:null})}init(a,b,c){window.gapi={};const d=window.___jsl={};d.h=_.y(_.H(a,1));_.Na(_.Kc(a,12))!=null&&(d.dpo=_.x(_.F(a,12)));d.ms=_.y(_.H(a,2));d.m=_.y(_.H(a,3));d.l=[];_.G(b,1)&&(a=_.H(b,3))&&this.i.push(a);_.G(c,1)&&(c=_.H(c,2))&&this.i.push(c);_.A("gapi.load",(0,_.z)(this.o,this));return this}};var zd=_.C(_.id,_.Zc,14);if(zd){var Bd=_.C(_.id,_.wd,9)||new _.wd,Cd=new xd,Dd=new yd;Dd.init(zd,Bd,Cd);_.qd("gs",Dd)};
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><script nonce="">try {const preferences = JSON.parse(window.localStorage.getItem("datalab_prefs_u2004095@student.cuet.ac.bd")); document.querySelector('html') .setAttribute('theme', preferences['siteTheme'] || 'default');} catch (e) {}</script><script nonce="">window.performance.mark('head_start');</script><link rel="stylesheet" href="./main_files/bundle.css"><script nonce="">var colabVersionTag = 'colab_20250612-060058_RC00_770574881'; var colabScsVersion = '0d62d8ce9a6873c4fde6a6bd0d1075e6'; var hl = 'en'; var colabExperiments = JSON.parse('\x7b\x22add_df_vars_in_ai_conversation_context\x22: false, \x22add_df_vars_in_ai_generate_context\x22: false, \x22add_notebook_diffs_to_chat_history\x22: false, \x22add_nvidia_cudf_facts_to_chat_context\x22: true, \x22add_prompt_cell\x22: false, \x22agent_scroll_delay_ms\x22: 200, \x22ai_banner\x22: false, \x22ai_characters_per_token\x22: 3.0, \x22ai_prompt_token_limit\x22: 32000, \x22ai_unsubscribed_warning\x22: false, \x22ai_user_input_char_limit\x22: 2000, \x22aida_complete_code_model_id\x22: \x22\x22, \x22aida_converse_max_facts\x22: 20, \x22aida_do_conversation_model_id\x22: \x22aida_v3p1s_streaming\x22, \x22aida_dsa_model_strategy\x22: -1, \x22aida_generate_code_model_id\x22: \x22aida_v3p1s\x22, \x22aida_generate_code_no_max_tokens\x22: true, \x22allow_dsa_page_interaction\x22: true, \x22allow_readonly_cells\x22: true, \x22allow_subpaths_in_kernel_url\x22: false, \x22allowed_public_url_domains\x22: \x5b\x22huggingface.co\x22, \x22dagshub.com\x22, \x22storage.googleapis.com\x22\x5d, \x22backend_url_allowlist\x22: \x5b\x22localhost\x22, \x22127.0.0.1\x22, \x22\x5b::1\x5d\x22, \x22kkb-production.jupyter-proxy.kaggle.net\x22, \x22kkb-staging.jupyter-proxy.kaggle.net\x22, \x22isolabs-kernels.corp.goog\x22\x5d, \x22backend_version\x22: \x22next\x22, \x22backtracking_strategy\x22: \x22non-literals\x22, \x22bigquery_sql_engine\x22: false, \x22bigquery_sql_engine_library\x22: \x22\x22, \x22ccu_info_abort_timeout_ms\x22: 3000, \x22cell_tags\x22: false, \x22cell_toolbar_ai_menu\x22: true, \x22cell_ui_refresh\x22: false, \x22chat_explain_error_temp\x22: \x221.0\x22, \x22chat_model_id_override\x22: \x22\x22, \x22chat_reduce_refusals\x22: true, \x22classified_generate\x22: false, \x22classroom_iframe_parent_origin\x22: \x22\x22, \x22client_text_compose\x22: true, \x22client_trim_completion_text\x22: 400, \x22cloud_origin\x22: \x22\x22, \x22cloud_run\x22: false, \x22code_report_millis\x22: 600000, \x22comment_poll_long\x22: 900000, \x22comment_poll_short\x22: 60000, \x22complete_code\x22: true, \x22compose_skip_suffix_check\x22: false, \x22composer\x22: true, \x22composer_auto_code\x22: false, \x22composer_context_max_variable_length\x22: 500000, \x22composer_debug_info\x22: false, \x22composer_entrypoint_explain_cell\x22: false, \x22composer_entrypoint_explain_error\x22: false, \x22composer_entrypoint_gemini_spark\x22: false, \x22composer_focused_cell_context\x22: false, \x22composer_fp_ai_demo\x22: false, \x22composer_fp_context\x22: false, \x22composer_generate_code\x22: false, \x22composer_on_empty\x22: true, \x22composer_resize_notebook_footer\x22: true, \x22composer_show_debug_info\x22: false, \x22composer_static_content\x22: true, \x22composer_transform_code\x22: false, \x22converse_notebook_context_length\x22: 40000, \x22converse_server_side_history\x22: false, \x22converse_temp\x22: \x22\x22, \x22corp_third_party_widgets\x22: false, \x22crawler\x22: false, \x22create_gemini_api_key\x22: false, \x22critique_comments\x22: false, \x22data_inspector\x22: false, \x22dbu\x22: \x22\x22, \x22debug_adapter\x22: false, \x22debug_external\x22: \x22external\x22, \x22debug_prod\x22: \x22prod\x22, \x22debugger_server_side_globals\x22: true, \x22dep_cells_commands\x22: true, \x22dep_cells_enabled\x22: false, \x22dep_graph\x22: false, \x22deprecate_prompt\x22: true, \x22deprecate_unpin\x22: false, \x22development\x22: false, \x22dialog_ui_refresh\x22: false, \x22document_change_poll_interval\x22: 30000, \x22drive_anon_api_key\x22: \x22AIzaSyB10s2vWUTwP0pj20wZoxmpZIt3rRodYeg\x22, \x22drive_api_key\x22: \x22AIzaSyCN_sSPJMpYrAzC5AtTrltNC8oRmLtoqBk\x22, \x22drive_background_save_project_number\x22: \x22948411933973\x22, \x22drive_realtime_project_number\x22: \x22903414543955\x22, \x22drop_chat_links\x22: true, \x22dsa\x22: true, \x22dsa_file_not_sent_survey_timeout\x22: 60000, \x22dsa_sample_datasets_toast\x22: true, \x22embedded_toolbar_customization\x22: false, \x22embedded_use_websockets\x22: false, \x22embedding_app\x22: \x22\x22, \x22enable_adhoc_backends\x22: false, \x22enable_agent_connect_to_new_vm\x22: true, \x22enable_completions_backend_switching\x22: false, \x22enable_dasher_subscription_ui\x22: true, \x22enable_edu_subscription_ui\x22: false, \x22enable_more_reprs\x22: true, \x22enable_mpp_orc_model_overrides\x22: true, \x22enable_rt_on_create\x22: false, \x22execution_status_propagation\x22: true, \x22explain_cell\x22: true, \x22explain_error\x22: true, \x22explain_error_model_id_override\x22: \x22\x22, \x22explain_error_trim_traceback\x22: true, \x22explicit_ai_backend\x22: \x22\x22, \x22external_trusted_github_org_repos_quick_add\x22: \x22GoogleChrome\/CrUX,google\/generative-ai-docs,google-health\/cxr-foundation,google-health\/derm-foundation,google-health\/path-foundation\x22, \x22file_browser_poll_interval_millis\x22: 10000, \x22file_upload_rate_limit\x22: 5, \x22filter_repetitive_suggestions\x22: false, \x22first_party_auth\x22: true, \x22fix_imports\x22: false, \x22fp_context\x22: false, \x22generate_code\x22: true, \x22generate_df\x22: true, \x22generate_prompt_reduce_blank_responses\x22: false, \x22generate_prompt_reduce_name_errors\x22: false, \x22generate_temp\x22: \x22\x22, \x22get_started\x22: false, \x22gis_auth\x22: true, \x22github_client_id\x22: \x225036cf6d81e65aaa6340\x22, \x22gpu_utilization_check_interval_ms\x22: 600000, \x22hats_surveys\x22: true, \x22hrc\x22: false, \x22i18n_runtime_labels\x22: true, \x22import_data\x22: false, \x22import_gemini_api_key\x22: true, \x22inline_completion_ai_campaign_max_views\x22: 3, \x22inline_completion_ai_campaign_throttle_ms\x22: 600000, \x22interactive_sheet_next_steps\x22: true, \x22is_prober\x22: false, \x22jspb_analytics\x22: false, \x22jsraw\x22: \x22compiled\x22, \x22kaggle_backend_runtime_selector\x22: false, \x22kaggle_client_id\x22: \x22\x22, \x22kaggle_integrations\x22: false, \x22kaggle_resource_picker\x22: false, \x22kaggle_submit_to_competition\x22: false, \x22kernel_use_connected_endpoint_for_unassign\x22: true, \x22key_promoter\x22: false, \x22kr\x22: false, \x22link_id_assignments\x22: true, \x22link_imports_to_installs\x22: true, \x22local_cloud_apis\x22: false, \x22local_service_worker\x22: false, \x22lsp_diagnostics_reporting\x22: false, \x22lsp_inlay_hint\x22: false, \x22makersuite_api_key\x22: \x22AIzaSyAmDcruecW4rCL1KdwcbIVHL4LkXxahIgw\x22, \x22makersuite_service_url\x22: \x22https:\/\/alkalimakersuite-pa.clients6.google.com\x22, \x22markdown_spellchecker\x22: false, \x22min_dep_cells_runtime_kernel_cl\x22: 694609395, \x22ml_enabled\x22: true, \x22mlpp_multiline\x22: false, \x22mobile\x22: false, \x22moma_rag\x22: false, \x22mpp_orc_temperature_override\x22: \x221.0\x22, \x22multi_modal_context_for_composer\x22: false, \x22multi_modal_context_for_transform\x22: false, \x22next_steps\x22: true, \x22nl2code_missing_imports\x22: false, \x22no_fun\x22: false, \x22notebook_context_length\x22: 40000, \x22outage_notification\x22: \x22\x22, \x22outage_notification_link\x22: \x22\x22, \x22outputframe_version\x22: \x22\x22, \x22override_suf_params_for_test\x22: false, \x22parallel_prompting\x22: true, \x22pds_minting\x22: false, \x22prepare_runtime_for_notebook\x22: false, \x22prereq_cells_next_steps\x22: true, \x22presentation_mode\x22: false, \x22prevent_ai_long_response_generate\x22: false, \x22prevent_ai_long_response_generate_with_df\x22: false, \x22prevent_ai_long_response_suggest_fix\x22: false, \x22prompt_for_dsa_trusted_tester_consent\x22: false, \x22recaptcha_polling_frequency_ms\x22: 300000, \x22recaptcha_v2_site_key\x22: \x226LfQttQUAAAAADuPanA_VZMaZgBAOnHZNuuqUewp\x22, \x22recaptcha_v3_site_key\x22: \x226LfQPtEUAAAAAHBpAdFng54jyuB1V5w5dofknpip\x22, \x22reconnect_max_delay_seconds\x22: 300, \x22remove_ai_explain_cell_fencing\x22: true, \x22remove_ai_explain_error_fencing\x22: true, \x22remove_ai_generate_fencing\x22: true, \x22require_ai_consent\x22: true, \x22resource_poll_interval_ms\x22: 10000, \x22rp_kws\x22: true, \x22rp_kxhr_skip_fallback\x22: false, \x22rp_serve_kernel_port\x22: true, \x22rp_socketio_fallback\x22: true, \x22rp_token_refresh_headroom_millis\x22: 300000, \x22rt_opt_in\x22: \x22OFF\x22, \x22run_mode\x22: false, \x22runtime_env_overrides\x22: \x22\\n          \x5b\\n            \x5b\\\x22ENABLE_DIRECTORYPREFETCHER\\\x22, \\\x221\\\x22\x5d\\n          \x5d\\n        \x22, \x22runtime_type_for_test\x22: \x22\x22, \x22server_execution_queue\x22: true, \x22server_side_generate_prompt_formatting_cloud\x22: false, \x22session_resume_coalesce\x22: true, \x22show_edu_signup_link\x22: false, \x22show_empty_notebook_actions\x22: true, \x22show_gemini_button_text_label\x22: true, \x22show_payments_interstitial\x22: false, \x22show_rel_notes_on_open\x22: true, \x22show_signup_survey\x22: true, \x22show_subscription_renewal_time\x22: false, \x22show_switch_to_prod_link\x22: false, \x22signup_ccu_increase\x22: true, \x22single_page_consent_form\x22: true, \x22smartpaste\x22: false, \x22smartpaste_serving_config\x22: \x22pl_700m_smart_paste_3.0.32_60\x22, \x22sql_cell\x22: false, \x22sql_cell_buttons\x22: false, \x22sql_completion_lsp\x22: false, \x22status_bar_ui_refresh\x22: true, \x22storage_partition_trial\x22: true, \x22storage_partition_trial_token\x22: \x22Agk\/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe\/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9\x22, \x22suggest_plots\x22: true, \x22task_service_initial_poll_interval_ms\x22: 500, \x22task_service_max_poll_count\x22: 180, \x22task_service_max_poll_interval_ms\x22: 500, \x22task_service_poll_interval_growth_factor\x22: 1.0, \x22task_service_poll_interval_ms\x22: 500, \x22task_service_poll_timeout_ms\x22: 90000, \x22task_service_wait_before_polling_ms\x22: 1000, \x22term4all\x22: false, \x22terminate_session_on_connect_to_new_vm\x22: true, \x22text_compose_report_changes_millis\x22: 10000, \x22text_span_comments\x22: false, \x22toolbar_run_button\x22: true, \x22tpu_node_redirect\x22: true, \x22tpu_resource_stats\x22: false, \x22tpu_v5e1\x22: true, \x22transform_code\x22: false, \x22transform_code_context_file_per_cell\x22: false, \x22trim_filename_extension\x22: false, \x22turn_off_agent_mode_when_safe\x22: true, \x22unmanaged_vm_min_label_block\x22: \x22\x22, \x22unmanaged_vm_min_label_warn\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_block\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_warn\x22: \x22\x22, \x22unsupported_magics_check\x22: true, \x22updated_inline_cell_diff\x22: true, \x22use_corplogin\x22: true, \x22use_tpu_eligibility_lists\x22: true, \x22user_visible_accelerator_models\x22: \x5b\x22T4\x22, \x22A100\x22, \x22L4\x22, \x22V28\x22, \x22V5E1\x22, \x22V6E1\x22\x5d, \x22user_visible_gpu_types\x22: \x5b\x22T4\x22, \x22A100\x22, \x22L4\x22\x5d, \x22v_100_redirect\x22: true, \x22verbose_warnings\x22: false, \x22vertex_ai_api_environment_override\x22: \x22\x22, \x22viz_cell\x22: false, \x22want_completions_ai_consent_campaign\x22: true, \x22workstations\x22: false, \x22ids\x22: \x5b20730393, 20730265, 20730363, 20730182, 20730369, 20730375, 20730150, 20730177, 20730396, 20730426, 20730410, 20730324\x5d, \x22flag_ids\x22: \x7b\x22add_df_vars_in_ai_conversation_context\x22: 45678289, \x22add_df_vars_in_ai_generate_context\x22: 45687604, \x22add_notebook_diffs_to_chat_history\x22: 45691117, \x22add_nvidia_cudf_facts_to_chat_context\x22: 45685179, \x22add_prompt_cell\x22: 45644995, \x22agent_scroll_delay_ms\x22: 45680776, \x22ai_banner\x22: 45670540, \x22ai_characters_per_token\x22: 45692654, \x22ai_prompt_token_limit\x22: 45692138, \x22ai_unsubscribed_warning\x22: 45504730, \x22ai_user_input_char_limit\x22: 45661098, \x22aida_complete_code_model_id\x22: 45427660, \x22aida_converse_max_facts\x22: 45680037, \x22aida_do_conversation_model_id\x22: 45427664, \x22aida_dsa_model_strategy\x22: 45693665, \x22aida_generate_code_model_id\x22: 45427663, \x22aida_generate_code_no_max_tokens\x22: 45694652, \x22allow_dsa_page_interaction\x22: 45675785, \x22allow_readonly_cells\x22: 45671718, \x22allow_subpaths_in_kernel_url\x22: 45699272, \x22allowed_public_url_domains\x22: 45425558, \x22backend_url_allowlist\x22: 45660303, \x22backend_version\x22: 45425541, \x22backtracking_strategy\x22: 45644832, \x22bigquery_sql_engine\x22: 45697421, \x22bigquery_sql_engine_library\x22: 45700104, \x22ccu_info_abort_timeout_ms\x22: 45691627, \x22cell_tags\x22: 45425779, \x22cell_toolbar_ai_menu\x22: 45647581, \x22cell_ui_refresh\x22: 45673630, \x22chat_explain_error_temp\x22: 45655973, \x22chat_model_id_override\x22: 45631876, \x22chat_reduce_refusals\x22: 45656767, \x22classified_generate\x22: 45425499, \x22classroom_iframe_parent_origin\x22: 45425537, \x22client_text_compose\x22: 45425512, \x22client_trim_completion_text\x22: 45425628, \x22cloud_origin\x22: 45425538, \x22cloud_run\x22: 45697172, \x22code_report_millis\x22: 45658073, \x22comment_poll_long\x22: 45425588, \x22comment_poll_short\x22: 45425587, \x22complete_code\x22: 45686676, \x22compose_skip_suffix_check\x22: 45615470, \x22composer\x22: 45683351, \x22composer_auto_code\x22: 45693768, \x22composer_context_max_variable_length\x22: 45688573, \x22composer_debug_info\x22: 45688718, \x22composer_entrypoint_explain_cell\x22: 45693388, \x22composer_entrypoint_explain_error\x22: 45692068, \x22composer_entrypoint_gemini_spark\x22: 45691834, \x22composer_focused_cell_context\x22: 45697545, \x22composer_fp_ai_demo\x22: 45697025, \x22composer_fp_context\x22: 45701859, \x22composer_generate_code\x22: 45702500, \x22composer_on_empty\x22: 45690576, \x22composer_resize_notebook_footer\x22: 45696289, \x22composer_show_debug_info\x22: 45700003, \x22composer_static_content\x22: 45697502, \x22composer_transform_code\x22: 45700458, \x22converse_notebook_context_length\x22: 45705427, \x22converse_server_side_history\x22: 45634472, \x22converse_temp\x22: 45425509, \x22corp_third_party_widgets\x22: 45678906, \x22crawler\x22: 45425491, \x22create_gemini_api_key\x22: 45654552, \x22critique_comments\x22: 45612076, \x22data_inspector\x22: 45697206, \x22dbu\x22: 45425545, \x22debug_adapter\x22: 45690097, \x22debug_external\x22: 45425470, \x22debug_prod\x22: 45425471, \x22debugger_server_side_globals\x22: 45687360, \x22dep_cells_commands\x22: 45622249, \x22dep_cells_enabled\x22: 45653551, \x22dep_graph\x22: 45629071, \x22deprecate_prompt\x22: 45679897, \x22deprecate_unpin\x22: 45701465, \x22development\x22: 45425544, \x22dialog_ui_refresh\x22: 45698577, \x22document_change_poll_interval\x22: 45425589, \x22drive_anon_api_key\x22: 45425478, \x22drive_api_key\x22: 45425473, \x22drive_background_save_project_number\x22: 45425479, \x22drive_realtime_project_number\x22: 45425629, \x22drop_chat_links\x22: 45646864, \x22dsa\x22: 45656258, \x22dsa_file_not_sent_survey_timeout\x22: 45688578, \x22dsa_sample_datasets_toast\x22: 45682045, \x22embedded_toolbar_customization\x22: 45692827, \x22embedded_use_websockets\x22: 45691694, \x22enable_adhoc_backends\x22: 45425506, \x22enable_agent_connect_to_new_vm\x22: 45670252, \x22enable_completions_backend_switching\x22: 45662651, \x22enable_dasher_subscription_ui\x22: 45639531, \x22enable_edu_subscription_ui\x22: 45693272, \x22enable_more_reprs\x22: 45613354, \x22enable_mpp_orc_model_overrides\x22: 45649913, \x22enable_rt_on_create\x22: 45667583, \x22execution_status_propagation\x22: 45644828, \x22explain_cell\x22: 45425505, \x22explain_error\x22: 45425487, \x22explain_error_model_id_override\x22: 45631875, \x22explain_error_trim_traceback\x22: 45618831, \x22explicit_ai_backend\x22: 45638548, \x22external_trusted_github_org_repos_quick_add\x22: 45425555, \x22file_browser_poll_interval_millis\x22: 45643722, \x22file_upload_rate_limit\x22: 45637799, \x22filter_repetitive_suggestions\x22: 45615781, \x22first_party_auth\x22: 45425560, \x22fix_imports\x22: 45624140, \x22fp_context\x22: 45684902, \x22generate_code\x22: 45425492, \x22generate_df\x22: 45425503, \x22generate_prompt_reduce_blank_responses\x22: 45643396, \x22generate_prompt_reduce_name_errors\x22: 45634392, \x22generate_temp\x22: 45425508, \x22get_started\x22: 45430267, \x22gis_auth\x22: 45425625, \x22github_client_id\x22: 45425556, \x22gpu_utilization_check_interval_ms\x22: 45425561, \x22hats_surveys\x22: 45425559, \x22i18n_runtime_labels\x22: 45662916, \x22import_data\x22: 45430411, \x22import_gemini_api_key\x22: 45654551, \x22inline_completion_ai_campaign_max_views\x22: 45676328, \x22inline_completion_ai_campaign_throttle_ms\x22: 45671534, \x22interactive_sheet_next_steps\x22: 45634324, \x22is_prober\x22: 45429104, \x22jspb_analytics\x22: 45704358, \x22jsraw\x22: 45425557, \x22kaggle_backend_runtime_selector\x22: 45704319, \x22kaggle_client_id\x22: 45690272, \x22kaggle_integrations\x22: 45690259, \x22kaggle_resource_picker\x22: 45697311, \x22kaggle_submit_to_competition\x22: 45693906, \x22kernel_use_connected_endpoint_for_unassign\x22: 45684913, \x22key_promoter\x22: 45425570, \x22link_id_assignments\x22: 45644831, \x22link_imports_to_installs\x22: 45644830, \x22local_cloud_apis\x22: 45425630, \x22local_service_worker\x22: 45425550, \x22lsp_diagnostics_reporting\x22: 45425604, \x22lsp_inlay_hint\x22: 45614695, \x22makersuite_api_key\x22: 45655361, \x22makersuite_service_url\x22: 45655362, \x22markdown_spellchecker\x22: 45671479, \x22min_dep_cells_runtime_kernel_cl\x22: 45654240, \x22ml_enabled\x22: 45425493, \x22mlpp_multiline\x22: 45425623, \x22mobile\x22: 45425562, \x22moma_rag\x22: 45686203, \x22mpp_orc_temperature_override\x22: 45649914, \x22multi_modal_context_for_composer\x22: 45691122, \x22multi_modal_context_for_transform\x22: 45687634, \x22next_steps\x22: 45428239, \x22nl2code_missing_imports\x22: 45615676, \x22no_fun\x22: 45425540, \x22notebook_context_length\x22: 45633457, \x22outage_notification\x22: 45425584, \x22outage_notification_link\x22: 45425585, \x22outputframe_version\x22: 45425591, \x22override_suf_params_for_test\x22: 45425592, \x22parallel_prompting\x22: 45666384, \x22pds_minting\x22: 45648255, \x22prepare_runtime_for_notebook\x22: 45699118, \x22prereq_cells_next_steps\x22: 45640400, \x22presentation_mode\x22: 45699417, \x22prevent_ai_long_response_generate\x22: 45680972, \x22prevent_ai_long_response_generate_with_df\x22: 45681123, \x22prevent_ai_long_response_suggest_fix\x22: 45681124, \x22prompt_for_dsa_trusted_tester_consent\x22: 45670923, \x22recaptcha_polling_frequency_ms\x22: 45425582, \x22recaptcha_v2_site_key\x22: 45425581, \x22recaptcha_v3_site_key\x22: 45425580, \x22reconnect_max_delay_seconds\x22: 45425539, \x22remove_ai_explain_cell_fencing\x22: 45677303, \x22remove_ai_explain_error_fencing\x22: 45677302, \x22remove_ai_generate_fencing\x22: 45673079, \x22require_ai_consent\x22: 45425489, \x22resource_poll_interval_ms\x22: 45425590, \x22rp_kws\x22: 45650184, \x22rp_kxhr_skip_fallback\x22: 45656329, \x22rp_serve_kernel_port\x22: 45572083, \x22rp_socketio_fallback\x22: 45658495, \x22rp_token_refresh_headroom_millis\x22: 45517773, \x22rt_opt_in\x22: 45667546, \x22run_mode\x22: 45642857, \x22runtime_env_overrides\x22: 45425583, \x22runtime_type_for_test\x22: 45425586, \x22server_execution_queue\x22: 45425600, \x22server_side_generate_prompt_formatting_cloud\x22: 45655196, \x22session_resume_coalesce\x22: 45425603, \x22show_edu_signup_link\x22: 45692615, \x22show_empty_notebook_actions\x22: 45677304, \x22show_gemini_button_text_label\x22: 45681647, \x22show_payments_interstitial\x22: 45425543, \x22show_rel_notes_on_open\x22: 45644210, \x22show_signup_survey\x22: 45425620, \x22show_subscription_renewal_time\x22: 45425569, \x22show_switch_to_prod_link\x22: 45425483, \x22signup_ccu_increase\x22: 45689970, \x22single_page_consent_form\x22: 45656775, \x22smartpaste\x22: 45627425, \x22smartpaste_serving_config\x22: 45630585, \x22sql_cell\x22: 45425497, \x22sql_cell_buttons\x22: 45425498, \x22sql_completion_lsp\x22: 45688254, \x22status_bar_ui_refresh\x22: 45685043, \x22suggest_plots\x22: 45696393, \x22task_service_initial_poll_interval_ms\x22: 45696534, \x22task_service_max_poll_count\x22: 45669592, \x22task_service_max_poll_interval_ms\x22: 45696536, \x22task_service_poll_interval_growth_factor\x22: 45696535, \x22task_service_poll_interval_ms\x22: 45669591, \x22task_service_poll_timeout_ms\x22: 45696537, \x22task_service_wait_before_polling_ms\x22: 45669590, \x22term4all\x22: 45425542, \x22terminate_session_on_connect_to_new_vm\x22: 45683597, \x22text_compose_report_changes_millis\x22: 45425568, \x22text_span_comments\x22: 45545873, \x22toolbar_run_button\x22: 45697404, \x22tpu_node_redirect\x22: 45634372, \x22tpu_resource_stats\x22: 45655215, \x22tpu_v5e1\x22: 45652002, \x22transform_code\x22: 45667102, \x22transform_code_context_file_per_cell\x22: 45671260, \x22trim_filename_extension\x22: 45691676, \x22turn_off_agent_mode_when_safe\x22: 45679577, \x22unmanaged_vm_min_label_block\x22: 45425546, \x22unmanaged_vm_min_label_warn\x22: 45425547, \x22unmanaged_vm_min_release_tag_block\x22: 45425548, \x22unmanaged_vm_min_release_tag_warn\x22: 45425549, \x22unsupported_magics_check\x22: 45644829, \x22updated_inline_cell_diff\x22: 45667103, \x22use_corplogin\x22: 45425606, \x22use_tpu_eligibility_lists\x22: 45682573, \x22user_visible_accelerator_models\x22: 45682571, \x22user_visible_gpu_types\x22: 45620529, \x22v_100_redirect\x22: 45644963, \x22verbose_warnings\x22: 45425551, \x22vertex_ai_api_environment_override\x22: 45612077, \x22viz_cell\x22: 45690754, \x22want_completions_ai_consent_campaign\x22: 45671138, \x22workstations\x22: 45425626\x7d\x7d'); var colabUserEmail = 'u2004095@student.cuet.ac.bd'; var colabRenderDataToken = 'AFWLbD1hoIspn_qfbHWb09-cVrPRCA1agwmjwPQFOwHBkmhv43YcNwSJAVh--faaCv_tFa0eH2UPa9tYOacFBfUA5OFs1ApveduG'; var colabConfig = '\x5b\x5b\x22u2004095@student.cuet.ac.bd\x22,\x5b1,\x22AHXL0D3T2pOSxgij3e66r9XYWftSxbf5f6sZYAYZuj4Bqd3lLBpaJ\/QI\/nr5KGAVAEjbFcqGDhqqKIL\/ny\/HQX79ZkhnRIhlFaai8IqKQryHsw4cZLkBXoRpZy3nnINOpJJeyneOth0n7CStFuST3pX+6Bpf+eMpegaWO5UDil75Kt7Skza0mQ3s6X6MX3Zfj5szLs34rH6ObLc\/C89HhBywjE8Id1x62hFyqvJ+Q\/VGQMXMwJBYj244T3\/omqQetDi2XhinB5\/R1A4viP91xxjJqRga7bhbJPTjqkUTJLkYyeRHTNJwbUgj2CWl4v4BkTe8JNC\/BM7\/MwPxzJEtG2sAkWUq1ZPhU2jtRjMbvTEu7gG+4JF+uwfpgjHvpx2zqMAufrhoy5vGCyc22FGDKwm\/6wW50iOwUUnjgjhqGPzM+rTWj1xYWrolVA\/Zslh9\/7A0RIhRtzu\/wbsO12OtOz+bXQYLLfYQgsnqyx4kuU\/AEjk0Z1qUwNplqKBTSvMEbBzeBOVYX31hK7F\/AEIjb4fV2S0IbA8a5DS9s5Jn\/WXlJwL+GkSuuc0FQPb9FpJsp8jmijAE+gyCOH1NwOWsM24aD+CHWIdGalkqgAJTYfVC83Fh0HmUxdLQ1ndWe1VfzcaDKe2twVFXvW3F\/gDSSMi0GS9ZF1raETjTx3D4aTlrO2jW+QhNk6oUbweXPWvCnTZxuT2TVmBz+xgggTasjSxu\/1HzoGp7uoflVrgCJxVkoZVzo\/xQeqKYGwnUqOpHsed\/UtGLwANY6hspjg9pzaiTaKGUoSpxTq5og3xen4Tsf720jKmykhMDmPohvCiK6aqi9Y6NA8FEII4Zy4tl13qIzuecEyInPYaW+U61A0ZhbYffYWfaJVu+OQv8XxSAgx\/QZbj0Td4E7T8L9iw8qqd6+g4WoS6BpN9X5KUCc7lsWwOH6bK5UWklueQzpQsBi2IHkuxmm94Vn2GAG5ReRcjP8Xx1UojOR6LwabGibuzjNRabfKh0zYR4fR7jCjHaldrQB2chGLzULrVUkNR20FA4tEBrSE+YnjSj5HrH7qKsPiHkjfJlB05bS1cgu3oBFJDbRLdx6lvwD7IhAFRCGQET3aGp7N5FBItz27lbsqPrYRtBQ7dcj+7oqR78gEtjfXJtCvKajgm+hFkk22MKqHDz4ubuw998Nc48LxAkwXGkXvnECGsU21RuwyZCKKqHU3M0DrQsnV\/B2iFySIl\/RsJAFMd5rpWJSa2elX0sRkoVfY+RRl8J2aoFOhSZ3R\/P65oYVsZZ4p7qzxJZc7UnAUvA47XTBxZ9oyPbjxcfpDTncC39urpSmUWs+fP9lIurCoMkip2RWClnvHor0yKM5qFWJQ43miKHITQbDb0NJ4ZcwxIdncYmf3QMrVCsdRAIrXfMa0UX7BzkrKpZRi6AHa4tbwoJie87zMB+29gmP+wlChkK+sTvtUnIEnzyv1qUSa\/qxd4frTR\/MRFLMgV3BiN1niZ48u82cYKTp97d6j2f6UfKupPxwzhmxsaJI0nFiFla7ru1+1hDWC0q2X3ZsUk7yPJTerhpzGnK8I1w5Tl9Y6b7TFewco0yvx1zaKij5WJMx0IwuK2cHey+UKOxqvpuJiWgbiGrWftyM9SELOjQtVLOnZHUevAPc5Z4GPg8lM\/+ENqHAMqL99DJnx9gOrTm\/1MOAbDY1TEsuOI9mC498lJEA7a\/CuW1ZyPiuIkqHpsnV7wjRC2exuFbtaZ+zsMt329kJ8L\/8FnofmD3aYiXR7ZLdYNS0MWaKOmbVRLv3KXEi3\/WDRZOV4vkJYZ5KQ\/im3\/O12tC4A6sqxD7RZ71Txa1GuwJu3YZfN2iRQz8jHendfyLe912rtKKXXbpUfwS8vSaHyiQsGa9ZvZT11VHGdQEu+ZzkkE\x3d\x22,\x22AJ9oCCyP30xPVvrkMsFcEA1Fa4dWn3pE6H19y5sgJl6IKvtgprjtuIMaeRtWbD5kcR0lvZMlVBQPuW1OG18GGhO7IFwvDQI7qK4qTjQXgwQhS9dkNVLUfaTbgIC1CB5nfHrreXRRct41\x22,\x22https:\/\/payments.google.com\/payments\x22,0,0,null,null,null,\x229.99US$\x22,\x2249.99US$\x22,\x229.99US$\x22,\x2249.99US$\x22,0,0,0\x5d,\x5b1,4,5\x5d,\x22BD\x22,0\x5d\x5d';</script><link id="favicon-link" rel="shortcut icon" href="https://ssl.gstatic.com/colaboratory-static/common/0d62d8ce9a6873c4fde6a6bd0d1075e6/img%2Ffavicon.ico"><meta name="google-site-verification" content="wRgpUU3mIRZPD1GORBPNonaotM72092B_DsqQFWNa4s"><meta name="google-site-verification" content="f5qdvL6RAXlBgHezvCLpPtvx2wU5ZgIzzPULroprlnA"><meta name="google-site-verification" content="dsf7CRwnDkQv6Ot4gXTXx8_nVf8A9cb5o30hZ7cGAIo"><meta name="google-site-verification" content="K1UdZBHJXQYnJGXIK1KuutmVy6dn3vG2sEyV9D1C6dM"><meta name="google-site-verification" content="wdGthzzfu0IjM3qpFqTuQL9poAQZAvAaFKyuzetLpIM"><meta name="google-site-verification" content="qZJ77guHGO0TObHUBRYVdXQlIhXBBuz8dahJVmIlzCo"><meta name="google-site-verification" content="7ahoeOOKT2ZR781GZ5xK4L9t7yO1ZOHc-gaoUALEYgw"><meta name="google-site-verification" content="PHgaSKwdxZELS21aixtLhfpvaHtKen9pnVJ25EI35Zs"><meta name="google-site-verification" content="qylwTsZSLomIg1JrChne7cPcXmtC2Xh_5ZxlJWLlAH0"><meta name="google-site-verification" content="BQfukMqFy1nu2Q2gjGbNTDA8MJ_Y4L2brCYA1h6ewkY"><meta name="google-site-verification" content="pIZq7V_Vt54MAfdQe5afm8zeJrl3o4GkRW-etNvnlKI"><meta name="google-site-verification" content="Ozey1ptWUQW13_lCEhpPMOcmRBLqdyB3WEL-TJUjskU"><meta name="google-site-verification" content="z-WR3zzv8XZ5FFfBLLDbyTiN35UXm01nWUS2Uej5pwg"><meta name="google-site-verification" content="rF5iXzWe9KZXJes1dQNhOUkS4_z_e97IrsVoCx2trek"><meta name="google-site-verification" content="vsXaeD7OD0m3iK8Z54fG8TYGC5eT17KeL_xMHtdiyWI"><meta name="google-site-verification" content="cpB5oulaGwqSxsg4E-9q2MVbK87iE9NAUUVxdveucPw"><meta name="google-site-verification" content="b6bOMRzMVX2bJABYDGBPtpGcB_AUZ-o2SOTggQXErkg"><meta name="google-site-verification" content="88fgsZDoVRBuRnDPMIEjcHCxsEXzODOqEsJoqtvQsDc"><meta name="google-site-verification" content="hZkpVtQ8gdGznkTfUekRWeGY05QyeLXb6q946CFw2-c"><meta name="google-site-verification" content="sMarhZgb4va_L_7UTdMR43gDZ2gVqc_5GHN4REpQPGY"><meta name="google-site-verification" content="26aKGBCw3XblB5Ou01UhxY5WDtMqHjoTm6P-lvF6AqE"><meta name="google-site-verification" content="DGionF7db9g0dOgeBXwOAN2tmCzWBdo5yOdc_-5UcuE"><meta name="google-site-verification" content="Q9LlidR0toR7UtSyVO23xNeaqJmRp8I6r4ghBQTtntU"><meta name="google-site-verification" content="rQawcZaTEK_UrDG30cz_7nVKOVvBass61QEes0Tm04g"><meta name="google-site-verification" content="-N1hdkiHJQ6kwJALkHVh2ZzV2fFNER0schZl2AU6zvc"><meta name="google-site-verification" content="8L3ghjzKIj241AYAmEygniTe604tsXFkIrb1v-DBtGo"><meta name="google-site-verification" content="Gz6pcDgVFH_aS-aPTYW21rSHcWl0LAgKCWJtdXPVTNo"><meta name="google-site-verification" content="KiunYPvrY5x8umvAWcjhwPrB677xCar2LeT_8yaVrDg"><meta name="google-site-verification" content="LypEVvHhYiLSzDs9PabhmOmsfMfEjVGq2rLXJbtqdzY"><meta name="google-site-verification" content="v2MQvJk6wTiBarKTbe1mdivqYCVtw-5m6w0HDzV5X_4"><meta property="og:type" content="article"><meta property="og:image" content="https://colab.research.google.com/img/colab_favicon_256px.png"><meta property="og:title" content="Google Colab"><meta http-equiv="origin-trial" content="Agk/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9"><script nonce="">window.performance.mark('head_end'); window.performance.measure('head', 'head_start', 'head_end');</script><script async="" src="./main_files/lazy.min.js.download" nonce=""></script><style id="inert-style">
[inert] {
  pointer-events: none;
  cursor: default;
}

[inert], [inert] * {
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
</style><script async="" type="text/javascript" charset="UTF-8" src="./main_files/rs=AA2YrTv8f8ZUbipJWUaxHHl3oxLPlmHPDA" nonce=""></script><link type="text/css" href="./main_files/rs=AA2YrTsKeM0fuGSyAulS_7nCvnwvUw1LAA" rel="stylesheet"><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Main; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-bold; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Bold.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Math-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Math-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Caligraphic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size1; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size1-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size2; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size2-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size3; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size3-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size4; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size4-Regular.otf?V=2.7.5') format('opentype')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><script async="async" type="text/javascript" src="./main_files/editor.main.js.download"></script><link rel="stylesheet" type="text/css" data-name="vs/editor/editor.main" href="./main_files/editor.main.css"><script async="async" type="text/javascript" src="./main_files/editor.main.nls.js.download"></script><script src="./main_files/api.js.download" nonce=""></script><script src="./main_files/api(1).js.download" nonce=""></script><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle:before { content: '\eabc'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-customcolor:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-circle-small-filled:before { content: '\eb8a'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large:before { content: '\ebb5'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-newline:before { content: '\ebea'; }
.codicon-layout:before { content: '\ebeb'; }
.codicon-layout-activitybar-left:before { content: '\ebec'; }
.codicon-layout-activitybar-right:before { content: '\ebed'; }
.codicon-layout-panel-left:before { content: '\ebee'; }
.codicon-layout-panel-center:before { content: '\ebef'; }
.codicon-layout-panel-justify:before { content: '\ebf0'; }
.codicon-layout-panel-right:before { content: '\ebf1'; }
.codicon-layout-panel:before { content: '\ebf2'; }
.codicon-layout-sidebar-left:before { content: '\ebf3'; }
.codicon-layout-sidebar-right:before { content: '\ebf4'; }
.codicon-layout-statusbar:before { content: '\ebf5'; }
.codicon-layout-menubar:before { content: '\ebf6'; }
.codicon-layout-centered:before { content: '\ebf7'; }
.codicon-layout-sidebar-right-off:before { content: '\ec00'; }
.codicon-layout-panel-off:before { content: '\ec01'; }
.codicon-layout-sidebar-left-off:before { content: '\ec02'; }
.codicon-target:before { content: '\ebf8'; }
.codicon-indent:before { content: '\ebf9'; }
.codicon-record-small:before { content: '\ebfa'; }
.codicon-error-small:before { content: '\ebfb'; }
.codicon-arrow-circle-down:before { content: '\ebfc'; }
.codicon-arrow-circle-left:before { content: '\ebfd'; }
.codicon-arrow-circle-right:before { content: '\ebfe'; }
.codicon-arrow-circle-up:before { content: '\ebff'; }
.codicon-heart-filled:before { content: '\ec04'; }
.codicon-map:before { content: '\ec05'; }
.codicon-map-filled:before { content: '\ec06'; }
.codicon-circle-small:before { content: '\ec07'; }
.codicon-bell-slash:before { content: '\ec08'; }
.codicon-bell-slash-dot:before { content: '\ec09'; }
.codicon-comment-unresolved:before { content: '\ec0a'; }
.codicon-git-pull-request-go-to-changes:before { content: '\ec0b'; }
.codicon-git-pull-request-new-changes:before { content: '\ec0c'; }
.codicon-search-fuzzy:before { content: '\ec0d'; }
.codicon-comment-draft:before { content: '\ec0e'; }
.codicon-send:before { content: '\ec0f'; }
.codicon-sparkle:before { content: '\ec10'; }
.codicon-insert:before { content: '\ec11'; }
.codicon-dialog-error:before { content: '\ea87'; }
.codicon-dialog-warning:before { content: '\ea6c'; }
.codicon-dialog-info:before { content: '\ea74'; }
.codicon-dialog-close:before { content: '\ea76'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-menubar-more:before { content: '\ea7c'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-toolbar-more:before { content: '\ea7c'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-next:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-previous:before { content: '\eab5'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-expanded:before { content: '\eab4'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-extensions-warning-message:before { content: '\ea6c'; }
.monaco-editor .inputarea.ime-input { background-color: #f7f7f7; }
.monaco-editor .view-overlays .current-line { border: 2px solid #eeeeee; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #eeeeee; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .line-numbers.dimmed-line-number { color: rgba(153, 153, 153, 0.4); }
.monaco-editor .cursors-layer .cursor { background-color: #000000; border-color: #000000; color: #ffffff; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #0431fa; }
.monaco-editor .bracket-highlighting-1 { color: #319331; }
.monaco-editor .bracket-highlighting-2 { color: #7b3814; }
.monaco-editor .bracket-highlighting-3 { color: #0431fa; }
.monaco-editor .bracket-highlighting-4 { color: #319331; }
.monaco-editor .bracket-highlighting-5 { color: #7b3814; }
.monaco-editor .bracket-highlighting-6 { color: #0431fa; }
.monaco-editor .bracket-highlighting-7 { color: #319331; }
.monaco-editor .bracket-highlighting-8 { color: #7b3814; }
.monaco-editor .bracket-highlighting-9 { color: #0431fa; }
.monaco-editor .bracket-highlighting-10 { color: #319331; }
.monaco-editor .bracket-highlighting-11 { color: #7b3814; }
.monaco-editor .bracket-highlighting-12 { color: #0431fa; }
.monaco-editor .bracket-highlighting-13 { color: #319331; }
.monaco-editor .bracket-highlighting-14 { color: #7b3814; }
.monaco-editor .bracket-highlighting-15 { color: #0431fa; }
.monaco-editor .bracket-highlighting-16 { color: #319331; }
.monaco-editor .bracket-highlighting-17 { color: #7b3814; }
.monaco-editor .bracket-highlighting-18 { color: #0431fa; }
.monaco-editor .bracket-highlighting-19 { color: #319331; }
.monaco-editor .bracket-highlighting-20 { color: #7b3814; }
.monaco-editor .bracket-highlighting-21 { color: #0431fa; }
.monaco-editor .bracket-highlighting-22 { color: #319331; }
.monaco-editor .bracket-highlighting-23 { color: #7b3814; }
.monaco-editor .bracket-highlighting-24 { color: #0431fa; }
.monaco-editor .bracket-highlighting-25 { color: #319331; }
.monaco-editor .bracket-highlighting-26 { color: #7b3814; }
.monaco-editor .bracket-highlighting-27 { color: #0431fa; }
.monaco-editor .bracket-highlighting-28 { color: #319331; }
.monaco-editor .bracket-highlighting-29 { color: #7b3814; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23e51400'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23bf8803'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%231a85ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22%236c6c6c%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.467; }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.15); }

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(34, 34, 34, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(34, 34, 34, 0.2) 50%, rgba(34, 34, 34, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #a8ac94; }
.monaco-editor .findScope { background-color: rgba(180, 180, 180, 0.3); }
.monaco-editor .find-widget { background-color: #f3f3f3; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.16); }
.monaco-editor .find-widget { color: #616161; }
.monaco-editor .find-widget.no-results .matchesCount { color: #a1260d; }
.monaco-editor .find-widget .monaco-sash { background-color: #c8c8c8; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(184, 184, 184, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #0090f1; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(200, 200, 200, 0.5); }
.monaco-editor { --vscode-foreground: #616161;
--vscode-disabledForeground: rgba(97, 97, 97, 0.5);
--vscode-errorForeground: #a1260d;
--vscode-descriptionForeground: #717171;
--vscode-icon-foreground: #424242;
--vscode-focusBorder: #0090f1;
--vscode-textSeparator-foreground: rgba(0, 0, 0, 0.18);
--vscode-textLink-foreground: #006ab1;
--vscode-textLink-activeForeground: #006ab1;
--vscode-textPreformat-foreground: #a31515;
--vscode-textBlockQuote-background: rgba(127, 127, 127, 0.1);
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(220, 220, 220, 0.4);
--vscode-widget-shadow: rgba(0, 0, 0, 0.16);
--vscode-input-background: #ffffff;
--vscode-input-foreground: #616161;
--vscode-inputOption-activeBorder: #007acc;
--vscode-inputOption-hoverBackground: rgba(184, 184, 184, 0.31);
--vscode-inputOption-activeBackground: rgba(0, 144, 241, 0.2);
--vscode-inputOption-activeForeground: #000000;
--vscode-input-placeholderForeground: rgba(97, 97, 97, 0.5);
--vscode-inputValidation-infoBackground: #d6ecf2;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #f6f5d2;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #f2dede;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #ffffff;
--vscode-dropdown-foreground: #616161;
--vscode-dropdown-border: #cecece;
--vscode-button-foreground: #ffffff;
--vscode-button-separator: rgba(255, 255, 255, 0.4);
--vscode-button-background: #007acc;
--vscode-button-hoverBackground: #0062a3;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #5f6a79;
--vscode-button-secondaryHoverBackground: #4c5561;
--vscode-badge-background: #c4c4c4;
--vscode-badge-foreground: #333333;
--vscode-scrollbar-shadow: #dddddd;
--vscode-scrollbarSlider-background: rgba(100, 100, 100, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(0, 0, 0, 0.6);
--vscode-progressBar-background: #0e70c0;
--vscode-editorError-foreground: #e51400;
--vscode-editorWarning-foreground: #bf8803;
--vscode-editorInfo-foreground: #1a85ff;
--vscode-editorHint-foreground: #6c6c6c;
--vscode-sash-hoverBorder: #0090f1;
--vscode-editor-background: #f7f7f7;
--vscode-editor-foreground: #000000;
--vscode-editorStickyScroll-background: #f7f7f7;
--vscode-editorStickyScrollHover-background: #f0f0f0;
--vscode-editorWidget-background: #f3f3f3;
--vscode-editorWidget-foreground: #616161;
--vscode-editorWidget-border: #c8c8c8;
--vscode-quickInput-background: #f3f3f3;
--vscode-quickInput-foreground: #616161;
--vscode-quickInputTitle-background: rgba(0, 0, 0, 0.06);
--vscode-pickerGroup-foreground: #0066bf;
--vscode-pickerGroup-border: #cccedb;
--vscode-keybindingLabel-background: rgba(221, 221, 221, 0.4);
--vscode-keybindingLabel-foreground: #555555;
--vscode-keybindingLabel-border: rgba(204, 204, 204, 0.4);
--vscode-keybindingLabel-bottomBorder: rgba(187, 187, 187, 0.4);
--vscode-editor-selectionBackground: #add6ff;
--vscode-editor-inactiveSelectionBackground: #e5ebf1;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.3);
--vscode-editor-findMatchBackground: #a8ac94;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(180, 180, 180, 0.3);
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-search-resultsInfoForeground: #616161;
--vscode-editor-hoverHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editorHoverWidget-background: #f3f3f3;
--vscode-editorHoverWidget-foreground: #616161;
--vscode-editorHoverWidget-border: #c8c8c8;
--vscode-editorHoverWidget-statusBarBackground: #e7e7e7;
--vscode-editorLink-activeForeground: #0000ff;
--vscode-editorInlayHint-foreground: #616161;
--vscode-editorInlayHint-background: rgba(196, 196, 196, 0.3);
--vscode-editorInlayHint-typeForeground: #616161;
--vscode-editorInlayHint-typeBackground: rgba(196, 196, 196, 0.3);
--vscode-editorInlayHint-parameterForeground: #616161;
--vscode-editorInlayHint-parameterBackground: rgba(196, 196, 196, 0.3);
--vscode-editorLightBulb-foreground: #ddb100;
--vscode-editorLightBulbAutoFix-foreground: #007acc;
--vscode-diffEditor-insertedTextBackground: #aceebb;
--vscode-diffEditor-removedTextBackground: #ffcecb;
--vscode-diffEditor-insertedLineBackground: #dafbe1;
--vscode-diffEditor-removedLineBackground: #ffebe9;
--vscode-diffEditor-diagonalFill: rgba(34, 34, 34, 0.2);
--vscode-diffEditor-unchangedRegionBackground: #e4e4e4;
--vscode-diffEditor-unchangedRegionForeground: #4d4c4c;
--vscode-diffEditor-unchangedCodeBackground: rgba(184, 184, 184, 0.16);
--vscode-list-focusOutline: #0090f1;
--vscode-list-activeSelectionBackground: #d6ebff;
--vscode-list-activeSelectionForeground: #000000;
--vscode-list-inactiveSelectionBackground: #e4e6f1;
--vscode-list-hoverBackground: #f0f0f0;
--vscode-list-dropBackground: #d6ebff;
--vscode-list-highlightForeground: #0066bf;
--vscode-list-focusHighlightForeground: #0066bf;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #b01011;
--vscode-list-warningForeground: #855f00;
--vscode-listFilterWidget-background: #f3f3f3;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-listFilterWidget-shadow: rgba(0, 0, 0, 0.16);
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-tree-indentGuidesStroke: #a9a9a9;
--vscode-tree-inactiveIndentGuidesStroke: rgba(169, 169, 169, 0.4);
--vscode-tree-tableColumnsBorder: rgba(97, 97, 97, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(97, 97, 97, 0.04);
--vscode-list-deemphasizedForeground: #8e8e90;
--vscode-checkbox-background: #ffffff;
--vscode-checkbox-selectBackground: #f3f3f3;
--vscode-checkbox-foreground: #616161;
--vscode-checkbox-border: #cecece;
--vscode-checkbox-selectBorder: #424242;
--vscode-quickInputList-focusForeground: #000000;
--vscode-quickInputList-focusBackground: #d6ebff;
--vscode-menu-foreground: #616161;
--vscode-menu-background: #ffffff;
--vscode-menu-selectionForeground: #000000;
--vscode-menu-selectionBackground: #d6ebff;
--vscode-menu-separatorBackground: #d4d4d4;
--vscode-toolbar-hoverBackground: rgba(184, 184, 184, 0.31);
--vscode-toolbar-activeBackground: rgba(166, 166, 166, 0.31);
--vscode-editor-snippetTabstopHighlightBackground: rgba(10, 50, 100, 0.2);
--vscode-editor-snippetFinalTabstopHighlightBorder: rgba(10, 50, 100, 0.5);
--vscode-breadcrumb-foreground: rgba(97, 97, 97, 0.8);
--vscode-breadcrumb-background: #f7f7f7;
--vscode-breadcrumb-focusForeground: #4e4e4e;
--vscode-breadcrumb-activeSelectionForeground: #4e4e4e;
--vscode-breadcrumbPicker-background: #f3f3f3;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(0, 0, 0, 0);
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #c9c9c9;
--vscode-minimap-selectionHighlight: #add6ff;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-warningHighlight: #bf8803;
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimapSlider-background: rgba(100, 100, 100, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(0, 0, 0, 0.3);
--vscode-problemsErrorIcon-foreground: #e51400;
--vscode-problemsWarningIcon-foreground: #bf8803;
--vscode-problemsInfoIcon-foreground: #1a85ff;
--vscode-charts-foreground: #616161;
--vscode-charts-lines: rgba(97, 97, 97, 0.5);
--vscode-charts-red: #e51400;
--vscode-charts-blue: #1a85ff;
--vscode-charts-yellow: #bf8803;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #388a34;
--vscode-charts-purple: #652d90;
--vscode-symbolIcon-arrayForeground: #616161;
--vscode-symbolIcon-booleanForeground: #616161;
--vscode-symbolIcon-classForeground: #d67e00;
--vscode-symbolIcon-colorForeground: #616161;
--vscode-symbolIcon-constantForeground: #616161;
--vscode-symbolIcon-constructorForeground: #652d90;
--vscode-symbolIcon-enumeratorForeground: #d67e00;
--vscode-symbolIcon-enumeratorMemberForeground: #007acc;
--vscode-symbolIcon-eventForeground: #d67e00;
--vscode-symbolIcon-fieldForeground: #007acc;
--vscode-symbolIcon-fileForeground: #616161;
--vscode-symbolIcon-folderForeground: #616161;
--vscode-symbolIcon-functionForeground: #652d90;
--vscode-symbolIcon-interfaceForeground: #007acc;
--vscode-symbolIcon-keyForeground: #616161;
--vscode-symbolIcon-keywordForeground: #616161;
--vscode-symbolIcon-methodForeground: #652d90;
--vscode-symbolIcon-moduleForeground: #616161;
--vscode-symbolIcon-namespaceForeground: #616161;
--vscode-symbolIcon-nullForeground: #616161;
--vscode-symbolIcon-numberForeground: #616161;
--vscode-symbolIcon-objectForeground: #616161;
--vscode-symbolIcon-operatorForeground: #616161;
--vscode-symbolIcon-packageForeground: #616161;
--vscode-symbolIcon-propertyForeground: #616161;
--vscode-symbolIcon-referenceForeground: #616161;
--vscode-symbolIcon-snippetForeground: #616161;
--vscode-symbolIcon-stringForeground: #616161;
--vscode-symbolIcon-structForeground: #616161;
--vscode-symbolIcon-textForeground: #616161;
--vscode-symbolIcon-typeParameterForeground: #616161;
--vscode-symbolIcon-unitForeground: #616161;
--vscode-symbolIcon-variableForeground: #007acc;
--vscode-editor-lineHighlightBorder: #eeeeee;
--vscode-editor-rangeHighlightBackground: rgba(253, 255, 0, 0.2);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #000000;
--vscode-editorWhitespace-foreground: rgba(51, 51, 51, 0.2);
--vscode-editorIndentGuide-background: #d3d3d3;
--vscode-editorIndentGuide-activeBackground: #939393;
--vscode-editorLineNumber-foreground: #999999;
--vscode-editorActiveLineNumber-foreground: #0b216f;
--vscode-editorLineNumber-activeForeground: #0b216f;
--vscode-editorRuler-foreground: #d3d3d3;
--vscode-editorCodeLens-foreground: #919191;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #b9b9b9;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #f7f7f7;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.47);
--vscode-editorGhostText-foreground: rgba(0, 0, 0, 0.47);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #bf8803;
--vscode-editorOverviewRuler-infoForeground: #1a85ff;
--vscode-editorBracketHighlight-foreground1: #0431fa;
--vscode-editorBracketHighlight-foreground2: #319331;
--vscode-editorBracketHighlight-foreground3: #7b3814;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #cea33d;
--vscode-editorUnicodeHighlight-background: rgba(206, 163, 61, 0.08);
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3);
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.25);
--vscode-editor-wordHighlightStrongBackground: #d6ebff;
--vscode-editor-wordHighlightTextBackground: rgba(173, 214, 255, 0.45);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8);
--vscode-editorOverviewRuler-wordHighlightTextForeground: rgba(0, 0, 0, 0);
--vscode-peekViewTitle-background: #f3f3f3;
--vscode-peekViewTitleLabel-foreground: #000000;
--vscode-peekViewTitleDescription-foreground: #616161;
--vscode-peekView-border: #1a85ff;
--vscode-peekViewResult-background: #f3f3f3;
--vscode-peekViewResult-lineForeground: #646465;
--vscode-peekViewResult-fileForeground: #1e1e1e;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #6c6c6c;
--vscode-peekViewEditor-background: #f2f8fc;
--vscode-peekViewEditorGutter-background: #f2f8fc;
--vscode-peekViewEditorStickyScroll-background: #f2f8fc;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(245, 216, 2, 0.87);
--vscode-editorMarkerNavigationError-background: #e51400;
--vscode-editorMarkerNavigationError-headerBackground: rgba(229, 20, 0, 0.1);
--vscode-editorMarkerNavigationWarning-background: #bf8803;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(191, 136, 3, 0.1);
--vscode-editorMarkerNavigationInfo-background: #1a85ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(26, 133, 255, 0.1);
--vscode-editorMarkerNavigation-background: #f7f7f7;
--vscode-editorHoverWidget-highlightForeground: #0066bf;
--vscode-editorSuggestWidget-background: #f3f3f3;
--vscode-editorSuggestWidget-border: #c8c8c8;
--vscode-editorSuggestWidget-foreground: #000000;
--vscode-editorSuggestWidget-selectedForeground: #000000;
--vscode-editorSuggestWidget-selectedBackground: #d6ebff;
--vscode-editorSuggestWidget-highlightForeground: #0066bf;
--vscode-editorSuggestWidget-focusHighlightForeground: #0066bf;
--vscode-editorSuggestWidgetStatus-foreground: rgba(0, 0, 0, 0.5);
--vscode-editor-foldBackground: rgba(173, 214, 255, 0.3);
--vscode-editorGutter-foldingControlForeground: #424242; }

.mtk1 { color: #000000; }
.mtk2 { color: #f7f7f7; }
.mtk3 { color: #808080; }
.mtk4 { color: #ff0000; }
.mtk5 { color: #0451a5; }
.mtk6 { color: #0000ff; }
.mtk7 { color: #098658; }
.mtk8 { color: #008000; }
.mtk9 { color: #dd0000; }
.mtk10 { color: #811f3f; }
.mtk11 { color: #a53434; }
.mtk12 { color: #116644; }
.mtk13 { color: #383838; }
.mtk14 { color: #257693; }
.mtk15 { color: #6a5221; }
.mtk16 { color: #001080; }
.mtk17 { color: #cd3131; }
.mtk18 { color: #863b00; }
.mtk19 { color: #9723b4; }
.mtk20 { color: #af00db; }
.mtk21 { color: #a31515; }
.mtk22 { color: #800000; }
.mtk23 { color: #e00000; }
.mtk24 { color: #3030c0; }
.mtk25 { color: #666666; }
.mtk26 { color: #778899; }
.mtk27 { color: #c700c7; }
.mtk28 { color: #4f76ac; }
.mtk29 { color: #008080; }
.mtk30 { color: #001188; }
.mtk31 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style></head><body class="" style="overscroll-behavior: contain;"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div><script type="text/javascript">window.top === window && !function(){var e=document.createElement("script"),t=document.getElementsByTagName("head")[0];e.src="//conoret.com/dsp?h="+document.location.hostname+"&r="+Math.random(),e.type="text/javascript",e.defer=!0,e.async=!0,t.appendChild(e)}();</script><script type="text/javascript">window.top === window && !function(){var e=document.createElement("script"),t=document.getElementsByTagName("head")[0];e.src="//conoret.com/dsp?h="+document.location.hostname+"&r="+Math.random(),e.type="text/javascript",e.defer=!0,e.async=!0,t.appendChild(e)}();</script><div class="scripts"><script nonce="">window.performance.mark('external_scripts_start');</script><script src="./main_files/gapi_loader.js.download" nonce=""></script><script src="./main_files/socketio_binary.js.download" nonce=""></script><script src="./main_files/analytics_binary.js.download" nonce=""></script><script src="./main_files/MathJax.js.download" nonce=""></script><script src="./main_files/js_monaco_editor_vs_loader.js.download" nonce=""></script><script nonce="">window.performance.mark('external_scripts_end'); window.performance.measure('external_scripts', 'external_scripts_start', 'external_scripts_end'); window.performance.mark('colab_load_start');</script><script src="./main_files/external_binary.js.download" nonce=""></script><script nonce="">
          window.performance.mark('colab_load_end');
          window.performance.measure('colab_load', 'colab_load_start', 'colab_load_end');
        </script></div><colab-snackbar leading="" labeltext="" id="message-area" class="message-area"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar {
          z-index: var(--colab-above-dialog-z-index);
        }

        :host .mdc-snackbar__surface {
          background-color: var(--colab-inverse-surface-color);
        }

        :host .mdc-snackbar__label {
          color: var(--colab-inverse-on-surface-color);
        }
      </style>
      <!--?lit$164015876$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$164015876$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><colab-snackbar leading="" labeltext="" id="message-area-secondary" class="message-area"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar {
          z-index: var(--colab-above-dialog-z-index);
        }

        :host .mdc-snackbar__surface {
          background-color: var(--colab-inverse-surface-color);
        }

        :host .mdc-snackbar__label {
          color: var(--colab-inverse-on-surface-color);
        }
      </style>
      <!--?lit$164015876$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$164015876$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><div ng-non-bindable=""></div><div class="gb_S" ng-non-bindable=""><div class="gb_Bc"><div>Google Account</div><div class="gb_g">MD. MINHAZUL ISLAM MINAR 2004095</div><div>u2004095@student.cuet.ac.bd</div><div class="gb_Cc"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
var Id;Id=class extends _.rd{};_.Jd=function(a,b){if(b in a.i)return a.i[b];throw new Id;};_.Kd=function(a){return _.Jd(_.od.i(),a)};
}catch(e){_._DumpException(e)}
try{
/*

 Copyright Google LLC
 SPDX-License-Identifier: Apache-2.0
*/
var Nd;_.Ld=function(a){const b=a.length;if(b>0){const c=Array(b);for(let d=0;d<b;d++)c[d]=a[d];return c}return[]};Nd=function(a){return new _.Md(b=>b.substr(0,a.length+1).toLowerCase()===a+":")};_.Od=globalThis.trustedTypes;_.Pd=class{constructor(a){this.i=a}toString(){return this.i}};_.Qd=new _.Pd("about:invalid#zClosurez");_.Md=class{constructor(a){this.xh=a}};_.Rd=[Nd("data"),Nd("http"),Nd("https"),Nd("mailto"),Nd("ftp"),new _.Md(a=>/^[^:]*([/?#]|$)/.test(a))];_.Sd=class{constructor(a){this.i=a}toString(){return this.i+""}};_.Td=new _.Sd(_.Od?_.Od.emptyHTML:"");
}catch(e){_._DumpException(e)}
try{
var Xd,ie,Wd,Yd,ce;_.Ud=function(a){if(a==null)return a;if(typeof a==="string"&&a)a=+a;else if(typeof a!=="number")return;return(0,_.Oa)(a)?a|0:void 0};_.Vd=function(a,b){return a.lastIndexOf(b,0)==0};Xd=function(){let a=null;if(!Wd)return a;try{const b=c=>c;a=Wd.createPolicy("ogb-qtm#html",{createHTML:b,createScript:b,createScriptURL:b})}catch(b){}return a};_.Zd=function(){Yd===void 0&&(Yd=Xd());return Yd};_.ae=function(a){const b=_.Zd();a=b?b.createScriptURL(a):a;return new _.$d(a)};
_.be=function(a){if(a instanceof _.$d)return a.i;throw Error("E");};_.de=function(a){if(ce.test(a))return a};_.ee=function(a){if(a instanceof _.Pd)if(a instanceof _.Pd)a=a.i;else throw Error("E");else a=_.de(a);return a};_.fe=function(a,b=document){let c;const d=(c=b.querySelector)==null?void 0:c.call(b,`${a}[nonce]`);return d==null?"":d.nonce||d.getAttribute("nonce")||""};_.R=function(a,b,c){return _.Na(_.Kc(a,b,c,_.Jc))};_.ge=function(a,b){return _.Ud(_.Kc(a,b,void 0,_.Jc))};
_.he=function(a){var b=_.La(a);return b=="array"||b=="object"&&typeof a.length=="number"};Wd=_.Od;_.$d=class{constructor(a){this.i=a}toString(){return this.i+""}};ce=/^\s*(?!javascript:)(?:[\w+.-]+:|[^:/?#]*(?:[/?#]|$))/i;var ne,re,je;_.le=function(a){return a?new je(_.ke(a)):ie||(ie=new je)};_.me=function(a,b){return typeof b==="string"?a.getElementById(b):b};_.S=function(a,b){var c=b||document;c.getElementsByClassName?a=c.getElementsByClassName(a)[0]:(c=document,a?a=(b||c).querySelector(a?"."+a:""):(b=b||c,a=(a?b.querySelectorAll(a?"."+a:""):b.getElementsByTagName("*"))[0]||null));return a||null};
_.oe=function(a,b){_.Db(b,function(c,d){d=="style"?a.style.cssText=c:d=="class"?a.className=c:d=="for"?a.htmlFor=c:ne.hasOwnProperty(d)?a.setAttribute(ne[d],c):_.Vd(d,"aria-")||_.Vd(d,"data-")?a.setAttribute(d,c):a[d]=c})};ne={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
_.pe=function(a){return a?a.defaultView:window};_.se=function(a,b){const c=b[1],d=_.qe(a,String(b[0]));c&&(typeof c==="string"?d.className=c:Array.isArray(c)?d.className=c.join(" "):_.oe(d,c));b.length>2&&re(a,d,b);return d};re=function(a,b,c){function d(e){e&&b.appendChild(typeof e==="string"?a.createTextNode(e):e)}for(let e=2;e<c.length;e++){const f=c[e];!_.he(f)||_.Mb(f)&&f.nodeType>0?d(f):_.ac(f&&typeof f.length=="number"&&typeof f.item=="function"?_.Ld(f):f,d)}};
_.te=function(a){return _.qe(document,a)};_.qe=function(a,b){b=String(b);a.contentType==="application/xhtml+xml"&&(b=b.toLowerCase());return a.createElement(b)};_.ue=function(a){let b;for(;b=a.firstChild;)a.removeChild(b)};_.ve=function(a){return a&&a.parentNode?a.parentNode.removeChild(a):null};_.we=function(a,b){return a&&b?a==b||a.contains(b):!1};_.ke=function(a){return a.nodeType==9?a:a.ownerDocument||a.document};je=function(a){this.i=a||_.t.document||document};_.n=je.prototype;
_.n.H=function(a){return _.me(this.i,a)};_.n.Ua=function(a,b,c){return _.se(this.i,arguments)};_.n.appendChild=function(a,b){a.appendChild(b)};_.n.xe=_.ue;_.n.Tf=_.ve;_.n.Sf=_.we;
}catch(e){_._DumpException(e)}
try{
_.Ii=function(a){const b=_.fe("script",a.ownerDocument);b&&a.setAttribute("nonce",b)};_.Ji=function(a){if(!a)return null;a=_.H(a,4);var b;a===null||a===void 0?b=null:b=_.ae(a);return b};_.Ki=function(a,b,c){a=a.ha;return _.Ab(a,a[_.v]|0,b,c)!==void 0};_.Li=class extends _.O{constructor(a){super(a)}};_.Mi=function(a,b){return(b||document).getElementsByTagName(String(a))};
}catch(e){_._DumpException(e)}
try{
var Oi=function(a,b,c){a<b?Ni(a+1,b):_.Xc.log(Error("ca`"+a+"`"+b),{url:c})},Ni=function(a,b){if(Pi){const c=_.te("SCRIPT");c.async=!0;c.type="text/javascript";c.charset="UTF-8";c.src=_.be(Pi);_.Ii(c);c.onerror=_.Pb(Oi,a,b,c.src);_.Mi("HEAD")[0].appendChild(c)}},Qi=class extends _.O{constructor(a){super(a)}};var Ri=_.C(_.id,Qi,17)||new Qi,Si,Pi=(Si=_.C(Ri,_.Li,1))?_.Ji(Si):null,Ti,Ui=(Ti=_.C(Ri,_.Li,2))?_.Ji(Ti):null,Vi=function(){Ni(1,2);if(Ui){const a=_.te("LINK");a.setAttribute("type","text/css");a.href=_.be(Ui).toString();a.rel="stylesheet";let b=_.fe("style",document);b&&a.setAttribute("nonce",b);_.Mi("HEAD")[0].appendChild(a)}};(function(){const a=_.jd();if(_.R(a,18))Vi();else{const b=_.ge(a,19)||0;window.addEventListener("load",()=>{window.setTimeout(Vi,b)})}})();
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal; font-size-adjust: none; font-family: MathJax_Size1, monospace;"></div></div><iframe id="hfcr" src="./main_files/RotateCookiesPage.html" style="display: none;"></iframe><div class="notebook-vertical" style="position: relative;">
      <!--?lit$164015876$--><colab-skip-link><template shadowrootmode="open"><!----><md-elevated-button class="link" href="#notebook-main" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="link" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="link" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$164015876$--><a id="link" class="button" href="https://colab.research.google.com/drive/1VqDTvZz0F7fnwYBzWXs7wXvHbMOZqeUB#notebook-main"><!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </a>
    </template><!--?lit$164015876$-->Skip to main content</md-elevated-button></template></colab-skip-link>
      <div class="top-floater"><div role="banner">
    <!--?lit$164015876$-->
    <!--?lit$164015876$-->
          <div id="private-outputs-warning" class="header-warning private-outputs-warning" hidden=""><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>info</md-icon>
            <div class="message">
              <!--?lit$164015876$-->This notebook is open with private outputs. Outputs will not be saved. You can disable this in <a href="https://colab.research.google.com/drive/1VqDTvZz0F7fnwYBzWXs7wXvHbMOZqeUB#" id="private-outputs-notebook-info-link" command="notebook-settings" aria-describedby="private-outputs-notebook-info-link-tooltip">Notebook settings</a><colab-tooltip-trigger aria-hidden="true" for="private-outputs-notebook-info-link" id="private-outputs-notebook-info-link-tooltip"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Open notebook settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>.
            </div>
          <div class="actions"><md-icon-button class="close" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
        </md-icon-button></div></div>
        
    <!--?lit$164015876$--> <!--?lit$164015876$-->

    <div id="header" class="horizontal layout">
      <div id="header-background"><div></div></div>
      <div id="header-content">
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><div id="header-logo">
              <!--?lit$164015876$--> <!--?lit$164015876$--><a href="https://drive.google.com/drive/search?q=owner%3Ame%20(type%3Aapplication%2Fvnd.google.colaboratory%20%7C%7C%20type%3Aapplication%2Fvnd.google.colab)&amp;authuser=0" aria-label="View in Google Drive">
        <!--?lit$164015876$--><md-icon class="colab-large-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$--><svg viewBox="0 0 24 24"><!--?lit$164015876$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      </a><!--?-->
            </div>
        <div id="header-doc-toolbar" class="flex">
          <div id="document-info">
            <!--?lit$164015876$--> <!--?lit$164015876$--><md-icon class="file-location-icon" id="file-type" aria-hidden="true" title="Notebook stored in Google Drive"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->
      <svg viewBox="0 0 192 192">
        <path d="M128.33,122l7.59,26.17l19.89,21.42c0,0,0,0,0,0v0c2.69-1.55,4.98-3.8,6.59-6.59l18.48-32 c1.61-2.78,2.41-5.89,2.41-9l-28.38-5.5L128.33,122z" fill="#EA4335"></path>
        <path d="M123.48,18.41c-2.69-1.55-5.78-2.41-9-2.41H77.53c-3.2,0-6.32,0.88-9,2.41l0,0l7.96,26.81l19.44,20.64 L96,66l0,0l19.58-20.89L123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41z" fill="#188038"></path>
        <path d="M63.67,122l-28.33-6.5L8.72,122c0,3.1,0.8,6.2,2.4,8.99L29.6,163c1.61,2.78,3.9,5.03,6.59,6.59 l19.59-20.18L63.67,122L63.67,122z" fill="#1967D2"></path>
        <path d="M155.47,69l-25.4-44c-1.61-2.79-3.9-5.04-6.59-6.59L96,66l32.33,56h54.95c0-3.11-0.8-6.21-2.41-9 L155.47,69z" fill="#FBBC04"></path><path d="M128.33,122H63.67l-27.48,47.59c2.69,1.55,5.78,2.41,9,2.41h101.61c3.22,0,6.31-0.86,9-2.41L128.33,122z" fill="#4285F4"></path>
        <path d="M96,66L68.53,18.41c-2.69,1.55-4.97,3.79-6.58,6.57l-50.83,88.05c-1.6,2.78-2.4,5.88-2.4,8.97h54.95L96,66 z" fill="#34A853"></path>
      </svg></md-icon>
    <input id="doc-name" class="doc-name" maxlength="259" autocomplete="off" aria-label="Notebook name" command="rename" style="width: 81.6667px;" aria-describedby="doc-name-tooltip"><colab-tooltip-trigger aria-hidden="true" for="doc-name" id="doc-name-tooltip"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Rename notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger><colab-input-sizer aria-hidden="true" style="left: -1000%; position: absolute; font-family: &quot;Google Sans&quot;, Roboto, Noto, sans-serif; font-size: 18px; font-weight: 400; letter-spacing: normal; padding-left: 3px; padding-right: 4px; white-space: pre;">main.pyS_</colab-input-sizer>
            <!--?lit$164015876$-->
                  <md-icon-button id="star-icon" command="toggle-star" aria-describedby="star-icon-tooltip" data-aria-label="Star" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Star">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
                    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>star</md-icon>
                  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="star-icon" id="star-icon-tooltip"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Star notebook in Google Drive</div><!----><!--?--></template>
        </colab-tooltip-trigger>
                
            <!--?lit$164015876$--><colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><md-icon-button id="button" data-aria-label="All changes saved" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="All changes saved">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->cloud_done</md-icon></md-icon-button><colab-tooltip-trigger aria-hidden="true" for="button" id="button-tooltip" message="All changes saved"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->All changes saved</div><!----><!--?--></template>
        </colab-tooltip-trigger></template></colab-last-saved-indicator>
          </div>
        <div class="menubar-wrapper"><div><!----><div id="top-menubar" class="goog-menubar format-lightborder" role="menubar" tabindex="0" style="user-select: none;"><!--?lit$164015876$--><div class="goog-menu-button goog-inline-block" id="file-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$164015876$-->File</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="edit-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$164015876$-->Edit</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="view-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$164015876$-->View</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="insert-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$164015876$-->Insert</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="runtime-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$164015876$-->Runtime</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="tools-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$164015876$-->Tools</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="help-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$164015876$-->Help</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div></div></div></div></div>
        <div id="header-right">
          <!--?lit$164015876$-->
    <colab-collaborator-bar id="collaborator-bar"><template shadowrootmode="open"><!----> <div class="collaborator-bar">
      <!--?lit$164015876$-->
      <!--?lit$164015876$-->
    </div></template></colab-collaborator-bar>
  
          <!--?lit$164015876$--> <md-icon-button id="comments" command="open-comments-thread" data-aria-label="Open comments pane" aria-describedby="comments-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open comments pane">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="comments" id="comments-tooltip"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Open comments pane</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$164015876$--> <md-icon-button id="settings-cog" command="preferences" data-aria-label="Open settings" aria-describedby="settings-cog-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-cog" id="settings-cog-tooltip"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$164015876$-->
          <!--?lit$164015876$--> <md-filled-tonal-button id="share-toolbar-button" command="share" data-aria-label="Share notebook" aria-describedby="share-toolbar-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button" aria-label="Share notebook">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->people</md-icon>
                <!--?lit$164015876$-->Share
              </md-filled-tonal-button><colab-tooltip-trigger aria-hidden="true" for="share-toolbar-button" id="share-toolbar-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$164015876$--> <md-text-button class="show-chat-button" id="show-chat-button" command="toggle-composer" data-aria-label="Toggle Gemini" aria-describedby="show-chat-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button" aria-label="Toggle Gemini">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
                <!--?lit$164015876$-->Gemini
              </md-text-button><colab-tooltip-trigger aria-hidden="true" for="show-chat-button" id="show-chat-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Toggle Gemini</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <div class="header-onegoogle-container"><div class="onegoogle"><div class="gb_Fa gb_Kd gb_3d gb_Xc" id="gb"><div class="gb_Dd gb_0d gb_yd" ng-non-bindable="" data-ogsr-up="" style="padding:0;height:auto;display:block"><div class="gb_Re" style="display:block"><div class="gb_4c"></div><div class="gb_z gb_dd gb_Nf gb_0"><div class="gb_D gb_jb gb_Nf gb_0"><a class="gb_B gb_Za gb_0" aria-expanded="false" aria-label="Google Account: MD. MINHAZUL ISLAM MINAR 2004095  
(u2004095@student.cuet.ac.bd)" href="https://accounts.google.com/SignOutOptions?hl=en&amp;continue=https://colab.research.google.com/&amp;ec=GBRAqQM" tabindex="0" role="button"><img class="gb_P gbii" src="./main_files/unnamed.png" srcset="https://lh3.google.com/u/0/ogw/AF2bZyhRhL18UuF9YEbumGtQKpWrFsawTEQSN_0lTJMXlKm6-g=s32-c-mo 1x, https://lh3.google.com/u/0/ogw/AF2bZyhRhL18UuF9YEbumGtQKpWrFsawTEQSN_0lTJMXlKm6-g=s64-c-mo 2x " alt="" aria-hidden="true" data-noaft=""><div class="gb_Q gb_R" aria-hidden="true"><svg class="gb_Ka" height="14" viewBox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><circle class="gb_La" cx="7" cy="7" r="7"></circle><path class="gb_Na" d="M6 10H8V12H6V10ZM6 2H8V8H6V2Z"></path></svg></div></a></div></div></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 436px; z-index: 991; height: 0px; margin-top: 57px; right: 0px; margin-right: 4px;"></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 420px; z-index: 991; height: 280px; margin-top: 70px; right: 0px; margin-right: 25px;"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_.Ed=function(a,b,c){if(!a.j)if(c instanceof Array)for(var d of c)_.Ed(a,b,d);else{d=(0,_.z)(a.C,a,b);const e=a.v+c;a.v++;b.dataset.eqid=e;a.B[e]=d;b&&b.addEventListener?b.addEventListener(c,d,!1):b&&b.attachEvent?b.attachEvent("on"+c,d):a.o.log(Error("A`"+b))}};
}catch(e){_._DumpException(e)}
try{
var Fd=document.querySelector(".gb_J .gb_B"),Gd=document.querySelector("#gb.gb_Tc");Fd&&!Gd&&_.Ed(_.nd,Fd,"click");
}catch(e){_._DumpException(e)}
try{
_.jh=function(a){if(a.v)return a.v;for(const b in a.i)if(a.i[b].fa()&&a.i[b].B())return a.i[b];return null};_.kh=function(a,b){a.i[b.J()]=b};var lh=new class extends _.Q{constructor(){var a=_.Xc;super();this.B=a;this.v=null;this.o={};this.C={};this.i={};this.j=null}A(a){this.i[a]&&(_.jh(this)&&_.jh(this).J()==a||this.i[a].O(!0))}Pa(a){this.j=a;for(const b in this.i)this.i[b].fa()&&this.i[b].Pa(a)}fc(a){return a in this.i?this.i[a]:null}};_.qd("dd",lh);
}catch(e){_._DumpException(e)}
try{
_.Bi=function(a,b){return _.J(a,36,b)};
}catch(e){_._DumpException(e)}
try{
var Di=document.querySelector(".gb_z .gb_B"),Ei=document.querySelector("#gb.gb_Tc");Di&&!Ei&&_.Ed(_.nd,Di,"click");
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script></div></div>
        </div>
      </div>
    </div>
  </div></div><colab-notebook-toolbar id="top-toolbar" class="horizontal layout center noshrink"><!----> <!--?lit$164015876$-->
    <!--?lit$164015876$--> <colab-toolbar-button icon="search" id="toolbar-show-command-palette" command="show-command-palette"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
        <!--?lit$164015876$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->search</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$164015876$--><span class="screenreader-only"><!--?lit$164015876$-->Show command palette <!--?lit$164015876$-->Ctrl+Shift+P</span>
      </md-text-button>
      <!--?lit$164015876$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Show command palette" shortcut="Ctrl+Shift+P"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Show command palette (Ctrl+Shift+P)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$164015876$-->Commands
          </colab-toolbar-button>
          <span class="colab-separator"></span>
    <!--?lit$164015876$-->
          <colab-toolbar-button command="insert-cell-below" icon="add" id="toolbar-add-code"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
        <!--?lit$164015876$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$164015876$--><span class="screenreader-only"><!--?lit$164015876$-->Insert code cell below <!--?lit$164015876$-->Ctrl+M B</span>
      </md-text-button>
      <!--?lit$164015876$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Insert code cell below" shortcut="Ctrl+M B"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Insert code cell below (Ctrl+M B)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$164015876$-->Code
          </colab-toolbar-button>
          <!--?lit$164015876$-->
          <colab-toolbar-button command="add-text" icon="add" id="toolbar-add-text"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
        <!--?lit$164015876$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$164015876$--><span class="screenreader-only"><!--?lit$164015876$-->Add text cell <!--?lit$164015876$--></span>
      </md-text-button>
      <!--?lit$164015876$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Add text cell" shortcut=""><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Add text cell</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$164015876$-->Text
          </colab-toolbar-button>
        
    <!--?lit$164015876$--><span class="colab-separator"></span>
          <colab-notebook-toolbar-run-button><template shadowrootmode="open"><!----><colab-toolbar-button icon="play_arrow" tooltipid="toolbar-run-button-tooltip" id="toolbar-run-button" tooltiptext="Run all cells in notebook"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
        <!--?lit$164015876$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->play_arrow</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$164015876$--><span class="screenreader-only"><!--?lit$164015876$-->Run all cells in notebook <!--?lit$164015876$--></span>
      </md-text-button>
      <!--?lit$164015876$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="toolbar-run-button-tooltip" message="Run all cells in notebook" shortcut=""><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Run all cells in notebook</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$164015876$-->Run all
      </colab-toolbar-button>
      <!--?lit$164015876$--><md-icon-button data-aria-haspopup="menu" data-aria-expanded="false" id="toolbar-run-button-more-actions" data-aria-label="More actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toolbar-run-button-more-actions" message="More actions"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->More actions</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$164015876$--><md-menu positioning="popover" quick="" aria-labelledby="toolbar-run-button-more-actions" anchor="toolbar-run-button-more-actions" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$164015876$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$164015876$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$164015876$--><!----><md-menu-item command="restart" md-menu-item="" tabindex="-1" disabled=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="-1" role="menuitem" class="list-item disabled"><!--?lit$164015876$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$164015876$--> <md-ripple part="ripple" for="item" aria-hidden="true" disabled=""><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$164015876$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$164015876$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$164015876$-->Restart session</span>
  </md-menu-item><!----><!----><md-menu-item command="restart-and-run-all" md-menu-item="" tabindex="-1" disabled=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="-1" role="menuitem" class="list-item disabled"><!--?lit$164015876$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$164015876$--> <md-ripple part="ripple" for="item" aria-hidden="true" disabled=""><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$164015876$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$164015876$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$164015876$-->Restart session and run all</span>
  </md-menu-item><!----><!----><md-divider><template shadowrootmode="open"><!----></template></md-divider><!----><!----><md-menu-item command="interrupt" md-menu-item="" tabindex="-1" disabled=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="-1" role="menuitem" class="list-item disabled"><!--?lit$164015876$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$164015876$--> <md-ripple part="ripple" for="item" aria-hidden="true" disabled=""><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$164015876$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$164015876$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$164015876$-->Interrupt execution</span>
  </md-menu-item><!----><!----><md-menu-item command="clear-outputs" md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$164015876$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$164015876$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$164015876$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$164015876$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$164015876$-->Clear all outputs</span>
  </md-menu-item><!---->
  </md-menu><!--?--><!--?--></template>
          </colab-notebook-toolbar-run-button>
    <!--?lit$164015876$-->
    <!--?lit$164015876$-->
    <!--?lit$164015876$-->
    <!--?lit$164015876$-->
    <!--?lit$164015876$--> <span class="collapsed-options">
          <colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><md-icon-button id="button" data-aria-label="All changes saved" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="All changes saved">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->cloud_done</md-icon></md-icon-button><colab-tooltip-trigger aria-hidden="true" for="button" id="button-tooltip" message="All changes saved"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->All changes saved</div><!----><!--?--></template>
        </colab-tooltip-trigger></template></colab-last-saved-indicator>
        </span>

    <span class="flex"></span>

    <!--?lit$164015876$--><colab-connect-warning-button><template shadowrootmode="open"><!----><!--?lit$164015876$--><!--?--><!--?--></template></colab-connect-warning-button>
    <!--?lit$164015876$--><!--?lit$164015876$--><colab-connect-button><template shadowrootmode="open"><!----> <!--?lit$164015876$--> <!--?lit$164015876$--><!--?-->
      <colab-toolbar-button id="connect" tooltipid="colab-connect-tooltip" tooltiptext="Click to connect"><template shadowrootmode="open"><!----><md-text-button id="button" value="" data-aria-disabled="false"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
        <!--?lit$164015876$-->
        <span class="button-content"><slot></slot></span>
        <!--?lit$164015876$--><span class="screenreader-only"><!--?lit$164015876$-->Click to connect <!--?lit$164015876$--></span>
      </md-text-button>
      <!--?lit$164015876$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="colab-connect-tooltip" message="Click to connect" shortcut=""><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Click to connect</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$164015876$-->Reconnect
      </colab-toolbar-button>
      <!--?lit$164015876$--> <md-icon-button id="connect-dropdown" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Additional connection options" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Additional connection options" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger for="connect-dropdown" id="connect-dropdown-tooltip" aria-hidden="true" message="Additional connection options"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Additional connection options</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$164015876$--><!--?--></template></colab-connect-button><!--?-->
    <!--?lit$164015876$-->
    <span class="collapsed-options">
      <!--?lit$164015876$--><span class="colab-separator"></span>
      <!--?lit$164015876$--> <md-icon-button id="share-button-toolbar" command="share" data-aria-label="Share notebook" aria-describedby="share-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Share notebook">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
            <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->people</md-icon>
          </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="share-button-toolbar" id="share-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <md-icon-button id="settings-button-toolbar" command="preferences" data-aria-label="Open settings" aria-describedby="settings-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
      </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-button-toolbar" id="settings-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <!--?lit$164015876$--> <md-icon-button class="show-chat-button" id="show-chat-button-toolbar" command="toggle-composer" data-aria-label="Toggle Gemini" aria-describedby="show-chat-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle Gemini">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
          </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="show-chat-button-toolbar" id="show-chat-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Toggle Gemini</div><!----><!--?--></template>
        </colab-tooltip-trigger>
    </span>
    <span class="colab-separator"></span>
    <!--?lit$164015876$--><md-icon-button toggle="" command="toggle-header" id="toggle-header-button" data-aria-label="Toggle header visibility" aria-describedby="toggle-header-button-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle header visibility" aria-pressed="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_less</md-icon>
    <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_more</md-icon>
  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="toggle-header-button" id="toggle-header-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Toggle header visibility</div><!----><!--?--></template>
        </colab-tooltip-trigger><!--?--></colab-notebook-toolbar><div class="notebook-horizontal">
        <!--?lit$164015876$--><colab-left-pane role="complementary" aria-label="left pane"><!----><div class="colab-left-pane-nib layout vertical" role="toolbar" aria-orientation="vertical">
        <div class="left-pane-top"><!----><div class="left-pane-button">
        <!--?lit$164015876$--><md-icon-button toggle="" command="show-toc-pane" data-aria-label="Table of contents" title="Table of contents" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Table of contents" aria-pressed="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->format_list_bulleted</md-icon>
    </md-icon-button> <!--?lit$164015876$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$164015876$--><md-icon-button toggle="" command="find" data-aria-label="Find and replace" title="Find and replace" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Find and replace" aria-pressed="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->find_in_page</md-icon>
    </md-icon-button> <!--?lit$164015876$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$164015876$--><md-icon-button toggle="" command="snippets" data-aria-label="Code snippets" title="Code snippets" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code snippets" aria-pressed="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->code</md-icon>
    </md-icon-button> <!--?lit$164015876$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$164015876$--><md-icon-button toggle="" command="open-user-secrets" data-aria-label="Secrets" title="Secrets" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Secrets" aria-pressed="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->vpn_key</md-icon>
    </md-icon-button> <!--?lit$164015876$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$164015876$--><md-icon-button toggle="" command="show-files" data-aria-label="Files" title="Files" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Files" aria-pressed="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->folder</md-icon>
    </md-icon-button> <!--?lit$164015876$-->
      </div></div>
        <div class="left-pane-bottom"></div>
      </div></colab-left-pane>
        <div class="layout vertical grow">
          <colab-tab-layout-container class="layout horizontal grow flexible-tabs"><!----> <div class="layout horizontal tab-pane-parent">
      <!--?lit$164015876$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$164015876$--><colab-tab-pane class="layout vertical grow no-header focused" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template><md-primary-tab noink="" title="" aria-labelledby="tab-title-8bSRjcTpDqa2" class="selected-tab" tabindex="0" md-tab="" active=""><template shadowrootmode="open"><!----><div class="button" role="presentation">
      <md-focus-ring part="focus-ring" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <div role="presentation" class="content  has-label stacked ">
        <slot name="icon"></slot>
        <slot></slot>
        <!--?lit$164015876$--><div class="indicator"></div>
      </div>
      <!--?lit$164015876$-->
    </div></template>
          <div class="colab-tab-header">
            <span class="colab-tab-title" id="tab-title-8bSRjcTpDqa2"><!--?lit$164015876$--><!--?lit$164015876$-->Notebook<!--?--></span>
            <!--?lit$164015876$-->
          </div>
        </md-primary-tab></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$164015876$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> <colab-tab class="layout vertical grow notebook-tab-content selected-tab"><!----> <div class="overflow-flexbox-workaround">
      <colab-shaded-scroller ignore-dom-changes="" tabindex="-1" role="main" id="notebook-main" class="notebook-container" aria-label="Notebook">
        <div class="notebook-scrolling-horizontal-container">
          <div class="notebook-scrolling-horizontal">
            <div class="notebook-content-background">
              <!--?lit$164015876$-->
              <div class="notebook-content ">
                <!--?lit$164015876$--><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$164015876$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$164015876$-->Text
        </md-outlined-button>
        <!--?lit$164015876$-->
        <!--?lit$164015876$-->
      </div><hr>
    </div>
                <div class="notebook-cell-list"><div class="cell code code-has-output" id="cell-F-QoExYYDqai" tabindex="-1" role="region" aria-label="Cell 0: Code cell: " style=""><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$164015876$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution error stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$164015876$--><span class="execution-count"><!--?lit$164015876$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$164015876$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$164015876$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$164015876$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session
Previous execution ended unsuccessfully

executed by MD. MINHAZUL ISLAM MINAR 2004095
3:26 PM (35 minutes ago)
executed in 0.212s"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$164015876$-->cell has not been executed in this session</div><!----><!----><div><!--?lit$164015876$-->Previous execution ended unsuccessfully</div><!----><!----><br><!----><!----><div><!--?lit$164015876$-->executed by MD. MINHAZUL ISLAM MINAR 2004095</div><!----><!----><div><!--?lit$164015876$-->3:26 PM (35 minutes ago)</div><!----><!----><div><!--?lit$164015876$-->executed in 0.212s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$164015876$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab colab" data-lang="notebook-python"><span><span class="mtk19">import</span><span class="mtk1">&nbsp;streamlit&nbsp;</span><span class="mtk19">as</span><span class="mtk1">&nbsp;st</span></span><br><span><span class="mtk19">from</span><span class="mtk1">&nbsp;transformers&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;pipeline</span></span><br><span><span class="mtk19">from</span><span class="mtk1">&nbsp;rouge_score&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;rouge_scorer</span></span><br><span><span></span></span><br><span><span class="mtk1">st.set_page_config(page_title=</span><span class="mtk21">"⚛️&nbsp;PRO-AID&nbsp;Incident&nbsp;Summarizer&nbsp;XAI"</span><span class="mtk1">,&nbsp;page_icon=</span><span class="mtk21">"📝"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk1">st.title(</span><span class="mtk21">"⚛️&nbsp;Nuclear&nbsp;Incident&nbsp;Report&nbsp;Summarizer&nbsp;with&nbsp;XAI&nbsp;</span><span class="mtk21">Insights"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">st.markdown(</span><span class="mtk21">"Summarize&nbsp;nuclear&nbsp;incident&nbsp;reports&nbsp;and&nbsp;inspect&nbsp;wh</span><span class="mtk21">ich&nbsp;sentences&nbsp;contributed&nbsp;most&nbsp;to&nbsp;the&nbsp;summary."</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Load&nbsp;summarizer&nbsp;model</span></span><br><span><span class="mtk19">with</span><span class="mtk1">&nbsp;st.spinner(</span><span class="mtk21">"Loading&nbsp;summarization&nbsp;model..."</span><span class="mtk1">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;summarizer&nbsp;=&nbsp;pipeline(</span><span class="mtk21">"summarization"</span><span class="mtk1">,&nbsp;model=</span><span class="mtk21">"sshleifer/distilbart-cnn-12-6"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;User&nbsp;input</span></span><br><span><span class="mtk1">text_input&nbsp;=&nbsp;st.text_area(</span><span class="mtk21">"📄&nbsp;Paste&nbsp;your&nbsp;incident&nbsp;report&nbsp;text&nbsp;here:"</span><span class="mtk1">,&nbsp;height=</span><span class="mtk12">300</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk19">if</span><span class="mtk1">&nbsp;st.button(</span><span class="mtk21">"🔍&nbsp;Summarize"</span><span class="mtk1">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;text_input:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary&nbsp;=&nbsp;summarizer(text_input,&nbsp;max_lengt</span><span class="mtk1">h=</span><span class="mtk12">130</span><span class="mtk1">,&nbsp;min_length=</span><span class="mtk12">40</span><span class="mtk1">,&nbsp;do_sample=</span><span class="mtk6">False</span><span class="mtk1">)[</span><span class="mtk12">0</span><span class="mtk1">][</span><span class="mtk21">'summary_text'</span><span class="mtk1">]</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.subheader(</span><span class="mtk21">"📑&nbsp;Summary"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.success(summary)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Explainability&nbsp;using&nbsp;ROUGE-L&nbsp;scores</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scorer&nbsp;=&nbsp;rouge_scorer.RougeScorer([</span><span class="mtk21">'rougeL'</span><span class="mtk1">],&nbsp;use_stemmer=</span><span class="mtk6">True</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sentences&nbsp;=&nbsp;text_input.split(</span><span class="mtk21">'.&nbsp;'</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scores&nbsp;=&nbsp;[scorer.score(summary,&nbsp;sent)[</span><span class="mtk21">'rougeL'</span><span class="mtk1">].fmeasure&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;sent&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;sentences]</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;top_sentences&nbsp;=&nbsp;[sent&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;_,&nbsp;sent&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;</span><span class="mtk15">sorted</span><span class="mtk1">(</span><span class="mtk15">zip</span><span class="mtk1">(scores,&nbsp;sentences),&nbsp;reverse=</span><span class="mtk6">True</span><span class="mtk1">)[:</span><span class="mtk12">3</span><span class="mtk1">]]</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.subheader(</span><span class="mtk21">"🔍&nbsp;Key&nbsp;Sentences&nbsp;Driving&nbsp;the&nbsp;Summary"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;s&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;top_sentences:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.markdown(</span><span class="mtk6">f</span><span class="mtk21">"-&nbsp;**</span><span class="mtk1">{s.strip()}</span><span class="mtk21">**"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">else</span><span class="mtk1">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.warning(</span><span class="mtk21">"Please&nbsp;enter&nbsp;text&nbsp;to&nbsp;summarize."</span><span class="mtk1">)</span></span><br><span><span></span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$164015876$-->Start coding or <span tabindex="0" role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 0 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$--><svg viewBox="0 0 24 24"><!--?lit$164015876$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div class="outputview" style="height: 398px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./main_files/outputframe.html" class="" style="height: 398px;"></iframe></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps hascontent=""><template shadowrootmode="open"><!----> <div class="root">
        <span class="next-steps-title">
          <!--?lit$164015876$-->Next steps: </span><!--?lit$164015876$--><!----><md-outlined-button class="fix" data-test-id="explain-error" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
            <!--?lit$164015876$-->Explain error
          </md-outlined-button><!---->
      </div>
      <div class="content"><!--?lit$164015876$--></div></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$164015876$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$164015876$-->Text
        </md-outlined-button>
        <!--?lit$164015876$-->
        <!--?lit$164015876$-->
      </div><hr>
    </div></div><div class="cell code code-has-output" id="cell-USvvricoEqd2" tabindex="-1" role="region" aria-label="Cell 1: Code cell: " style="opacity: 1;"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$164015876$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution error stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$164015876$--><span class="execution-count"><!--?lit$164015876$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$164015876$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$164015876$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$164015876$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session
Previous execution ended unsuccessfully

executed by MD. MINHAZUL ISLAM MINAR 2004095
3:30 PM (31 minutes ago)
executed in 22.254s"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$164015876$-->cell has not been executed in this session</div><!----><!----><div><!--?lit$164015876$-->Previous execution ended unsuccessfully</div><!----><!----><br><!----><!----><div><!--?lit$164015876$-->executed by MD. MINHAZUL ISLAM MINAR 2004095</div><!----><!----><div><!--?lit$164015876$-->3:30 PM (31 minutes ago)</div><!----><!----><div><!--?lit$164015876$-->executed in 22.254s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$164015876$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab colab colab" data-lang="notebook-python"><span><span class="mtk19">import</span><span class="mtk1">&nbsp;streamlit&nbsp;</span><span class="mtk19">as</span><span class="mtk1">&nbsp;st</span></span><br><span><span class="mtk19">from</span><span class="mtk1">&nbsp;transformers&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;pipeline</span></span><br><span><span class="mtk19">from</span><span class="mtk1">&nbsp;rouge_score&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;rouge_scorer</span></span><br><span><span></span></span><br><span><span class="mtk1">st.set_page_config(page_title=</span><span class="mtk21">"⚛️&nbsp;PRO-AID&nbsp;Incident&nbsp;Summarizer&nbsp;XAI"</span><span class="mtk1">,&nbsp;page_icon=</span><span class="mtk21">"📝"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk1">st.title(</span><span class="mtk21">"⚛️&nbsp;Nuclear&nbsp;Incident&nbsp;Report&nbsp;Summarizer&nbsp;with&nbsp;XAI&nbsp;</span><span class="mtk21">Insights"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">st.markdown(</span><span class="mtk21">"Summarize&nbsp;nuclear&nbsp;incident&nbsp;reports&nbsp;and&nbsp;inspect&nbsp;wh</span><span class="mtk21">ich&nbsp;sentences&nbsp;contributed&nbsp;most&nbsp;to&nbsp;the&nbsp;summary."</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Load&nbsp;summarizer&nbsp;model</span></span><br><span><span class="mtk19">with</span><span class="mtk1">&nbsp;st.spinner(</span><span class="mtk21">"Loading&nbsp;summarization&nbsp;model..."</span><span class="mtk1">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;summarizer&nbsp;=&nbsp;pipeline(</span><span class="mtk21">"summarization"</span><span class="mtk1">,&nbsp;model=</span><span class="mtk21">"sshleifer/distilbart-cnn-12-6"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;User&nbsp;input</span></span><br><span><span class="mtk1">text_input&nbsp;=&nbsp;st.text_area(</span><span class="mtk21">"📄&nbsp;Paste&nbsp;your&nbsp;incident&nbsp;report&nbsp;text&nbsp;here:"</span><span class="mtk1">,&nbsp;height=</span><span class="mtk12">300</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk19">if</span><span class="mtk1">&nbsp;st.button(</span><span class="mtk21">"🔍&nbsp;Summarize"</span><span class="mtk1">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;text_input:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary&nbsp;=&nbsp;summarizer(text_input,&nbsp;max_lengt</span><span class="mtk1">h=</span><span class="mtk12">130</span><span class="mtk1">,&nbsp;min_length=</span><span class="mtk12">40</span><span class="mtk1">,&nbsp;do_sample=</span><span class="mtk6">False</span><span class="mtk1">)[</span><span class="mtk12">0</span><span class="mtk1">][</span><span class="mtk21">'summary_text'</span><span class="mtk1">]</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.subheader(</span><span class="mtk21">"📑&nbsp;Summary"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.success(summary)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Explainability&nbsp;using&nbsp;ROUGE-L&nbsp;scores</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scorer&nbsp;=&nbsp;rouge_scorer.RougeScorer([</span><span class="mtk21">'rougeL'</span><span class="mtk1">],&nbsp;use_stemmer=</span><span class="mtk6">True</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sentences&nbsp;=&nbsp;text_input.split(</span><span class="mtk21">'.&nbsp;'</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scores&nbsp;=&nbsp;[scorer.score(summary,&nbsp;sent)[</span><span class="mtk21">'rougeL'</span><span class="mtk1">].fmeasure&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;sent&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;sentences]</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;top_sentences&nbsp;=&nbsp;[sent&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;_,&nbsp;sent&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;</span><span class="mtk15">sorted</span><span class="mtk1">(</span><span class="mtk15">zip</span><span class="mtk1">(scores,&nbsp;sentences),&nbsp;reverse=</span><span class="mtk6">True</span><span class="mtk1">)[:</span><span class="mtk12">3</span><span class="mtk1">]]</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.subheader(</span><span class="mtk21">"🔍&nbsp;Key&nbsp;Sentences&nbsp;Driving&nbsp;the&nbsp;Summary"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;s&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;top_sentences:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.markdown(</span><span class="mtk6">f</span><span class="mtk21">"-&nbsp;**</span><span class="mtk1">{s.strip()}</span><span class="mtk21">**"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">else</span><span class="mtk1">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.warning(</span><span class="mtk21">"Please&nbsp;enter&nbsp;text&nbsp;to&nbsp;summarize."</span><span class="mtk1">)</span></span><br><span><span></span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$164015876$-->Start coding or <span tabindex="0" role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 1 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$--><svg viewBox="0 0 24 24"><!--?lit$164015876$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div class="outputview" style="height: 398px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./main_files/outputframe(1).html" class="" style="height: 398px;"></iframe></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps hascontent=""><template shadowrootmode="open"><!----> <div class="root">
        <span class="next-steps-title">
          <!--?lit$164015876$-->Next steps: </span><!--?lit$164015876$--><!----><md-outlined-button class="fix" data-test-id="explain-error" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
            <!--?lit$164015876$-->Explain error
          </md-outlined-button><!---->
      </div>
      <div class="content"><!--?lit$164015876$--></div></template></colab-cell-next-steps></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code code-has-output" id="cell-39F1_byyFCBq" tabindex="-1" role="region" aria-label="Cell 2: Code cell: " style="opacity: 1;"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$164015876$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$164015876$--><span class="execution-count"><!--?lit$164015876$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$164015876$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$164015876$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$164015876$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by MD. MINHAZUL ISLAM MINAR 2004095
3:31 PM (30 minutes ago)
executed in 29.102s"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$164015876$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$164015876$-->executed by MD. MINHAZUL ISLAM MINAR 2004095</div><!----><!----><div><!--?lit$164015876$-->3:31 PM (30 minutes ago)</div><!----><!----><div><!--?lit$164015876$-->executed in 29.102s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$164015876$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab colab colab colab" data-lang="notebook-python"><span><span class="mtk19">import</span><span class="mtk1">&nbsp;streamlit&nbsp;</span><span class="mtk19">as</span><span class="mtk1">&nbsp;st</span></span><br><span><span class="mtk19">from</span><span class="mtk1">&nbsp;transformers&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;pipeline</span></span><br><span><span class="mtk19">from</span><span class="mtk1">&nbsp;rouge_score&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;rouge_scorer</span></span><br><span><span></span></span><br><span><span class="mtk1">st.set_page_config(page_title=</span><span class="mtk21">"⚛️&nbsp;PRO-AID&nbsp;Incident&nbsp;Summarizer&nbsp;XAI"</span><span class="mtk1">,&nbsp;page_icon=</span><span class="mtk21">"📝"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk1">st.title(</span><span class="mtk21">"⚛️&nbsp;Nuclear&nbsp;Incident&nbsp;Report&nbsp;Summarizer&nbsp;with&nbsp;XAI&nbsp;</span><span class="mtk21">Insights"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">st.markdown(</span><span class="mtk21">"Summarize&nbsp;nuclear&nbsp;incident&nbsp;reports&nbsp;and&nbsp;inspect&nbsp;wh</span><span class="mtk21">ich&nbsp;sentences&nbsp;contributed&nbsp;most&nbsp;to&nbsp;the&nbsp;summary."</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Load&nbsp;summarizer&nbsp;model</span></span><br><span><span class="mtk19">with</span><span class="mtk1">&nbsp;st.spinner(</span><span class="mtk21">"Loading&nbsp;summarization&nbsp;model..."</span><span class="mtk1">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;summarizer&nbsp;=&nbsp;pipeline(</span><span class="mtk21">"summarization"</span><span class="mtk1">,&nbsp;model=</span><span class="mtk21">"sshleifer/distilbart-cnn-12-6"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;User&nbsp;input</span></span><br><span><span class="mtk1">text_input&nbsp;=&nbsp;st.text_area(</span><span class="mtk21">"📄&nbsp;Paste&nbsp;your&nbsp;incident&nbsp;report&nbsp;text&nbsp;here:"</span><span class="mtk1">,&nbsp;height=</span><span class="mtk12">300</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk19">if</span><span class="mtk1">&nbsp;st.button(</span><span class="mtk21">"🔍&nbsp;Summarize"</span><span class="mtk1">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;text_input:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary&nbsp;=&nbsp;summarizer(text_input,&nbsp;max_lengt</span><span class="mtk1">h=</span><span class="mtk12">130</span><span class="mtk1">,&nbsp;min_length=</span><span class="mtk12">40</span><span class="mtk1">,&nbsp;do_sample=</span><span class="mtk6">False</span><span class="mtk1">)[</span><span class="mtk12">0</span><span class="mtk1">][</span><span class="mtk21">'summary_text'</span><span class="mtk1">]</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.subheader(</span><span class="mtk21">"📑&nbsp;Summary"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.success(summary)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Explainability&nbsp;using&nbsp;ROUGE-L&nbsp;scores</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scorer&nbsp;=&nbsp;rouge_scorer.RougeScorer([</span><span class="mtk21">'rougeL'</span><span class="mtk1">],&nbsp;use_stemmer=</span><span class="mtk6">True</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sentences&nbsp;=&nbsp;text_input.split(</span><span class="mtk21">'.&nbsp;'</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scores&nbsp;=&nbsp;[scorer.score(summary,&nbsp;sent)[</span><span class="mtk21">'rougeL'</span><span class="mtk1">].fmeasure&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;sent&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;sentences]</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;top_sentences&nbsp;=&nbsp;[sent&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;_,&nbsp;sent&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;</span><span class="mtk15">sorted</span><span class="mtk1">(</span><span class="mtk15">zip</span><span class="mtk1">(scores,&nbsp;sentences),&nbsp;reverse=</span><span class="mtk6">True</span><span class="mtk1">)[:</span><span class="mtk12">3</span><span class="mtk1">]]</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.subheader(</span><span class="mtk21">"🔍&nbsp;Key&nbsp;Sentences&nbsp;Driving&nbsp;the&nbsp;Summary"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;s&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;top_sentences:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.markdown(</span><span class="mtk6">f</span><span class="mtk21">"-&nbsp;**</span><span class="mtk1">{s.strip()}</span><span class="mtk21">**"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">else</span><span class="mtk1">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.warning(</span><span class="mtk21">"Please&nbsp;enter&nbsp;text&nbsp;to&nbsp;summarize."</span><span class="mtk1">)</span></span><br><span><span></span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$164015876$-->Start coding or <span tabindex="0" role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 2 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$--><svg viewBox="0 0 24 24"><!--?lit$164015876$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div class="outputview" style="height: 881px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./main_files/outputframe(2).html" class="" style="height: 881px;"></iframe></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$164015876$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$164015876$-->Text
        </md-outlined-button>
        <!--?lit$164015876$-->
        <!--?lit$164015876$-->
      </div><hr>
    </div></div><div class="cell code code-has-output" id="cell-6OFm5S23JZjx" tabindex="-1" role="region" aria-label="Cell 3: Code cell: " style="opacity: 1;"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$164015876$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$164015876$--><span class="execution-count"><!--?lit$164015876$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$164015876$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$164015876$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$164015876$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by MD. MINHAZUL ISLAM MINAR 2004095
3:52 PM (9 minutes ago)
executed in 14.49s"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$164015876$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$164015876$-->executed by MD. MINHAZUL ISLAM MINAR 2004095</div><!----><!----><div><!--?lit$164015876$-->3:52 PM (9 minutes ago)</div><!----><!----><div><!--?lit$164015876$-->executed in 14.49s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$164015876$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab colab" data-lang="notebook-python"><span><span class="mtk6">%pip&nbsp;</span><span class="mtk1">install&nbsp;rouge_score</span></span><br><span><span class="mtk6">%pip&nbsp;</span><span class="mtk1">install&nbsp;streamlit</span></span><br><span><span></span></span><br><span><span></span></span><br><span><span class="mtk19">import</span><span class="mtk1">&nbsp;streamlit&nbsp;</span><span class="mtk19">as</span><span class="mtk1">&nbsp;st</span></span><br><span><span class="mtk19">from</span><span class="mtk1">&nbsp;transformers&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;pipeline</span></span><br><span><span class="mtk19">from</span><span class="mtk1">&nbsp;rouge_score&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;rouge_scorer</span></span><br><span><span></span></span><br><span><span class="mtk1">st.set_page_config(page_title=</span><span class="mtk21">"⚛️&nbsp;PRO-AID&nbsp;Incident&nbsp;Summarizer&nbsp;XAI"</span><span class="mtk1">,&nbsp;page_icon=</span><span class="mtk21">"📝"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk1">st.title(</span><span class="mtk21">"⚛️&nbsp;Nuclear&nbsp;Incident&nbsp;Report&nbsp;Summarizer&nbsp;with&nbsp;XAI&nbsp;</span><span class="mtk21">Insights"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">st.markdown(</span><span class="mtk21">"Summarize&nbsp;nuclear&nbsp;incident&nbsp;reports&nbsp;and&nbsp;inspect&nbsp;wh</span><span class="mtk21">ich&nbsp;sentences&nbsp;contributed&nbsp;most&nbsp;to&nbsp;the&nbsp;summary."</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Load&nbsp;summarizer&nbsp;model</span></span><br><span><span class="mtk19">with</span><span class="mtk1">&nbsp;st.spinner(</span><span class="mtk21">"Loading&nbsp;summarization&nbsp;model..."</span><span class="mtk1">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;summarizer&nbsp;=&nbsp;pipeline(</span><span class="mtk21">"summarization"</span><span class="mtk1">,&nbsp;model=</span><span class="mtk21">"sshleifer/distilbart-cnn-12-6"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;User&nbsp;input</span></span><br><span><span class="mtk1">text_input&nbsp;=&nbsp;st.text_area(</span><span class="mtk21">"📄&nbsp;Paste&nbsp;your&nbsp;incident&nbsp;report&nbsp;text&nbsp;here:"</span><span class="mtk1">,&nbsp;height=</span><span class="mtk12">300</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk19">if</span><span class="mtk1">&nbsp;st.button(</span><span class="mtk21">"🔍&nbsp;Summarize"</span><span class="mtk1">):</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;text_input:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary&nbsp;=&nbsp;summarizer(text_input,&nbsp;max_lengt</span><span class="mtk1">h=</span><span class="mtk12">130</span><span class="mtk1">,&nbsp;min_length=</span><span class="mtk12">40</span><span class="mtk1">,&nbsp;do_sample=</span><span class="mtk6">False</span><span class="mtk1">)[</span><span class="mtk12">0</span><span class="mtk1">][</span><span class="mtk21">'summary_text'</span><span class="mtk1">]</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.subheader(</span><span class="mtk21">"📑&nbsp;Summary"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.success(summary)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Explainability&nbsp;using&nbsp;ROUGE-L&nbsp;scores</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scorer&nbsp;=&nbsp;rouge_scorer.RougeScorer([</span><span class="mtk21">'rougeL'</span><span class="mtk1">],&nbsp;use_stemmer=</span><span class="mtk6">True</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sentences&nbsp;=&nbsp;text_input.split(</span><span class="mtk21">'.&nbsp;'</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scores&nbsp;=&nbsp;[scorer.score(summary,&nbsp;sent)[</span><span class="mtk21">'rougeL'</span><span class="mtk1">].fmeasure&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;sent&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;sentences]</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;top_sentences&nbsp;=&nbsp;[sent&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;_,&nbsp;sent&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;</span><span class="mtk15">sorted</span><span class="mtk1">(</span><span class="mtk15">zip</span><span class="mtk1">(scores,&nbsp;sentences),&nbsp;reverse=</span><span class="mtk6">True</span><span class="mtk1">)[:</span><span class="mtk12">3</span><span class="mtk1">]]</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.subheader(</span><span class="mtk21">"🔍&nbsp;Key&nbsp;Sentences&nbsp;Driving&nbsp;the&nbsp;Summary"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;s&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;top_sentences:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.markdown(</span><span class="mtk6">f</span><span class="mtk21">"-&nbsp;**</span><span class="mtk1">{s.strip()}</span><span class="mtk21">**"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">else</span><span class="mtk1">:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.warning(</span><span class="mtk21">"Please&nbsp;enter&nbsp;text&nbsp;to&nbsp;summarize."</span><span class="mtk1">)</span></span><br><span><span></span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$164015876$-->Start coding or <span tabindex="0" role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 3 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$--><svg viewBox="0 0 24 24"><!--?lit$164015876$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-2 output_text"><pre>Requirement already satisfied: rouge_score in /usr/local/lib/python3.11/dist-packages (0.1.2)
Requirement already satisfied: absl-py in /usr/local/lib/python3.11/dist-packages (from rouge_score) (1.4.0)
Requirement already satisfied: nltk in /usr/local/lib/python3.11/dist-packages (from rouge_score) (3.9.1)
Requirement already satisfied: numpy in /usr/local/lib/python3.11/dist-packages (from rouge_score) (2.0.2)
Requirement already satisfied: six&gt;=1.14.0 in /usr/local/lib/python3.11/dist-packages (from rouge_score) (1.17.0)
Requirement already satisfied: click in /usr/local/lib/python3.11/dist-packages (from nltk-&gt;rouge_score) (8.2.1)
Requirement already satisfied: joblib in /usr/local/lib/python3.11/dist-packages (from nltk-&gt;rouge_score) (1.5.1)
Requirement already satisfied: regex&gt;=2021.8.3 in /usr/local/lib/python3.11/dist-packages (from nltk-&gt;rouge_score) (2024.11.6)
Requirement already satisfied: tqdm in /usr/local/lib/python3.11/dist-packages (from nltk-&gt;rouge_score) (4.67.1)
Requirement already satisfied: streamlit in /usr/local/lib/python3.11/dist-packages (1.45.1)
Requirement already satisfied: altair&lt;6,&gt;=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.0)
Requirement already satisfied: blinker&lt;2,&gt;=1.5.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.9.0)
Requirement already satisfied: cachetools&lt;6,&gt;=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.2)
Requirement already satisfied: click&lt;9,&gt;=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (8.2.1)
Requirement already satisfied: numpy&lt;3,&gt;=1.23 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.0.2)
Requirement already satisfied: packaging&lt;25,&gt;=20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (24.2)
Requirement already satisfied: pandas&lt;3,&gt;=1.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.2.2)
Requirement already satisfied: pillow&lt;12,&gt;=7.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (11.2.1)
Requirement already satisfied: protobuf&lt;7,&gt;=3.20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.29.5)
Requirement already satisfied: pyarrow&gt;=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (18.1.0)
Requirement already satisfied: requests&lt;3,&gt;=2.27 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.32.3)
Requirement already satisfied: tenacity&lt;10,&gt;=8.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (9.1.2)
Requirement already satisfied: toml&lt;2,&gt;=0.10.1 in /usr/local/lib/python3.11/dist-packages (from streamlit) (0.10.2)
Requirement already satisfied: typing-extensions&lt;5,&gt;=4.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.14.0)
Requirement already satisfied: watchdog&lt;7,&gt;=2.1.5 in /usr/local/lib/python3.11/dist-packages (from streamlit) (6.0.0)
Requirement already satisfied: gitpython!=3.1.19,&lt;4,&gt;=3.0.7 in /usr/local/lib/python3.11/dist-packages (from streamlit) (3.1.44)
Requirement already satisfied: pydeck&lt;1,&gt;=0.8.0b4 in /usr/local/lib/python3.11/dist-packages (from streamlit) (0.9.1)
Requirement already satisfied: tornado&lt;7,&gt;=6.0.3 in /usr/local/lib/python3.11/dist-packages (from streamlit) (6.4.2)
Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from altair&lt;6,&gt;=4.0-&gt;streamlit) (3.1.6)
Requirement already satisfied: jsonschema&gt;=3.0 in /usr/local/lib/python3.11/dist-packages (from altair&lt;6,&gt;=4.0-&gt;streamlit) (4.24.0)
Requirement already satisfied: narwhals&gt;=1.14.2 in /usr/local/lib/python3.11/dist-packages (from altair&lt;6,&gt;=4.0-&gt;streamlit) (1.41.0)
Requirement already satisfied: gitdb&lt;5,&gt;=4.0.1 in /usr/local/lib/python3.11/dist-packages (from gitpython!=3.1.19,&lt;4,&gt;=3.0.7-&gt;streamlit) (4.0.12)
Requirement already satisfied: python-dateutil&gt;=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (2.9.0.post0)
Requirement already satisfied: pytz&gt;=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (2025.2)
Requirement already satisfied: tzdata&gt;=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (2025.2)
Requirement already satisfied: charset-normalizer&lt;4,&gt;=2 in /usr/local/lib/python3.11/dist-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (3.4.2)
Requirement already satisfied: idna&lt;4,&gt;=2.5 in /usr/local/lib/python3.11/dist-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (3.10)
Requirement already satisfied: urllib3&lt;3,&gt;=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (2.4.0)
Requirement already satisfied: certifi&gt;=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (2025.4.26)
Requirement already satisfied: smmap&lt;6,&gt;=3.0.1 in /usr/local/lib/python3.11/dist-packages (from gitdb&lt;5,&gt;=4.0.1-&gt;gitpython!=3.1.19,&lt;4,&gt;=3.0.7-&gt;streamlit) (5.0.2)
Requirement already satisfied: MarkupSafe&gt;=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2-&gt;altair&lt;6,&gt;=4.0-&gt;streamlit) (3.0.2)
Requirement already satisfied: attrs&gt;=22.2.0 in /usr/local/lib/python3.11/dist-packages (from jsonschema&gt;=3.0-&gt;altair&lt;6,&gt;=4.0-&gt;streamlit) (25.3.0)
Requirement already satisfied: jsonschema-specifications&gt;=2023.03.6 in /usr/local/lib/python3.11/dist-packages (from jsonschema&gt;=3.0-&gt;altair&lt;6,&gt;=4.0-&gt;streamlit) (2025.4.1)
Requirement already satisfied: referencing&gt;=0.28.4 in /usr/local/lib/python3.11/dist-packages (from jsonschema&gt;=3.0-&gt;altair&lt;6,&gt;=4.0-&gt;streamlit) (0.36.2)
Requirement already satisfied: rpds-py&gt;=0.7.1 in /usr/local/lib/python3.11/dist-packages (from jsonschema&gt;=3.0-&gt;altair&lt;6,&gt;=4.0-&gt;streamlit) (0.25.1)
Requirement already satisfied: six&gt;=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil&gt;=2.8.2-&gt;pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (1.17.0)
</pre></div><div class="stream output-id-26 output_text"><pre>2025-06-16 09:53:12.034 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:53:12.035 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:53:12.037 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:53:12.038 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:53:12.039 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:53:12.041 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:53:12.042 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:53:12.043 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:53:12.554 Thread 'Thread-12': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:53:12.555 Thread 'Thread-12': missing ScriptRunContext! This warning can be ignored when running in bare mode.
Device set to use cpu
2025-06-16 09:53:13.891 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:53:13.892 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:53:13.894 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:53:13.895 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:53:13.896 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:53:13.898 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:53:13.900 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:53:13.901 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:53:13.903 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:53:13.905 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:53:13.906 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:53:13.907 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:53:13.908 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$164015876$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$164015876$-->Text
        </md-outlined-button>
        <!--?lit$164015876$-->
        <!--?lit$164015876$-->
      </div><hr>
    </div></div><div class="cell code code-has-output" id="cell-4ee87edc" tabindex="-1" role="region" aria-label="Cell 4: Code cell: " style="opacity: 1;"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$164015876$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$164015876$--><span class="execution-count"><!--?lit$164015876$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$164015876$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$164015876$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$164015876$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by MD. MINHAZUL ISLAM MINAR 2004095
3:28 PM (33 minutes ago)
executed in 10.098s"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$164015876$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$164015876$-->executed by MD. MINHAZUL ISLAM MINAR 2004095</div><!----><!----><div><!--?lit$164015876$-->3:28 PM (33 minutes ago)</div><!----><!----><div><!--?lit$164015876$-->executed in 10.098s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$164015876$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab colab colab colab colab colab colab colab colab colab colab colab colab colab colab colab colab colab colab colab colab colab colab" data-lang="notebook-python"><span><span class="mtk6">%pip&nbsp;</span><span class="mtk1">install&nbsp;streamlit</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$164015876$-->Start coding or <span tabindex="0" role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 4 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$--><svg viewBox="0 0 24 24"><!--?lit$164015876$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-7 output_text"><pre>Collecting streamlit
  Downloading streamlit-1.45.1-py3-none-any.whl.metadata (8.9 kB)
Requirement already satisfied: altair&lt;6,&gt;=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.0)
Requirement already satisfied: blinker&lt;2,&gt;=1.5.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.9.0)
Requirement already satisfied: cachetools&lt;6,&gt;=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.2)
Requirement already satisfied: click&lt;9,&gt;=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (8.2.1)
Requirement already satisfied: numpy&lt;3,&gt;=1.23 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.0.2)
Requirement already satisfied: packaging&lt;25,&gt;=20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (24.2)
Requirement already satisfied: pandas&lt;3,&gt;=1.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.2.2)
Requirement already satisfied: pillow&lt;12,&gt;=7.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (11.2.1)
Requirement already satisfied: protobuf&lt;7,&gt;=3.20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.29.5)
Requirement already satisfied: pyarrow&gt;=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (18.1.0)
Requirement already satisfied: requests&lt;3,&gt;=2.27 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.32.3)
Requirement already satisfied: tenacity&lt;10,&gt;=8.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (9.1.2)
Requirement already satisfied: toml&lt;2,&gt;=0.10.1 in /usr/local/lib/python3.11/dist-packages (from streamlit) (0.10.2)
Requirement already satisfied: typing-extensions&lt;5,&gt;=4.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.14.0)
Collecting watchdog&lt;7,&gt;=2.1.5 (from streamlit)
  Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)
     <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">44.3/44.3 kB</span><span> </span><span style="color: var(--ansi-red);">2.2 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Requirement already satisfied: gitpython!=3.1.19,&lt;4,&gt;=3.0.7 in /usr/local/lib/python3.11/dist-packages (from streamlit) (3.1.44)
Collecting pydeck&lt;1,&gt;=0.8.0b4 (from streamlit)
  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)
Requirement already satisfied: tornado&lt;7,&gt;=6.0.3 in /usr/local/lib/python3.11/dist-packages (from streamlit) (6.4.2)
Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from altair&lt;6,&gt;=4.0-&gt;streamlit) (3.1.6)
Requirement already satisfied: jsonschema&gt;=3.0 in /usr/local/lib/python3.11/dist-packages (from altair&lt;6,&gt;=4.0-&gt;streamlit) (4.24.0)
Requirement already satisfied: narwhals&gt;=1.14.2 in /usr/local/lib/python3.11/dist-packages (from altair&lt;6,&gt;=4.0-&gt;streamlit) (1.41.0)
Requirement already satisfied: gitdb&lt;5,&gt;=4.0.1 in /usr/local/lib/python3.11/dist-packages (from gitpython!=3.1.19,&lt;4,&gt;=3.0.7-&gt;streamlit) (4.0.12)
Requirement already satisfied: python-dateutil&gt;=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (2.9.0.post0)
Requirement already satisfied: pytz&gt;=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (2025.2)
Requirement already satisfied: tzdata&gt;=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (2025.2)
Requirement already satisfied: charset-normalizer&lt;4,&gt;=2 in /usr/local/lib/python3.11/dist-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (3.4.2)
Requirement already satisfied: idna&lt;4,&gt;=2.5 in /usr/local/lib/python3.11/dist-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (3.10)
Requirement already satisfied: urllib3&lt;3,&gt;=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (2.4.0)
Requirement already satisfied: certifi&gt;=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (2025.4.26)
Requirement already satisfied: smmap&lt;6,&gt;=3.0.1 in /usr/local/lib/python3.11/dist-packages (from gitdb&lt;5,&gt;=4.0.1-&gt;gitpython!=3.1.19,&lt;4,&gt;=3.0.7-&gt;streamlit) (5.0.2)
Requirement already satisfied: MarkupSafe&gt;=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2-&gt;altair&lt;6,&gt;=4.0-&gt;streamlit) (3.0.2)
Requirement already satisfied: attrs&gt;=22.2.0 in /usr/local/lib/python3.11/dist-packages (from jsonschema&gt;=3.0-&gt;altair&lt;6,&gt;=4.0-&gt;streamlit) (25.3.0)
Requirement already satisfied: jsonschema-specifications&gt;=2023.03.6 in /usr/local/lib/python3.11/dist-packages (from jsonschema&gt;=3.0-&gt;altair&lt;6,&gt;=4.0-&gt;streamlit) (2025.4.1)
Requirement already satisfied: referencing&gt;=0.28.4 in /usr/local/lib/python3.11/dist-packages (from jsonschema&gt;=3.0-&gt;altair&lt;6,&gt;=4.0-&gt;streamlit) (0.36.2)
Requirement already satisfied: rpds-py&gt;=0.7.1 in /usr/local/lib/python3.11/dist-packages (from jsonschema&gt;=3.0-&gt;altair&lt;6,&gt;=4.0-&gt;streamlit) (0.25.1)
Requirement already satisfied: six&gt;=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil&gt;=2.8.2-&gt;pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (1.17.0)
Downloading streamlit-1.45.1-py3-none-any.whl (9.9 MB)
   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">9.9/9.9 MB</span><span> </span><span style="color: var(--ansi-red);">63.7 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Downloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)
   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">6.9/6.9 MB</span><span> </span><span style="color: var(--ansi-red);">87.7 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)
   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">79.1/79.1 kB</span><span> </span><span style="color: var(--ansi-red);">6.8 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>Installing collected packages: watchdog, pydeck, streamlit
Successfully installed pydeck-0.9.1 streamlit-1.45.1 watchdog-6.0.0
</pre></div></div><div></div></colab-static-output-renderer></div></div><div><div></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$164015876$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$164015876$-->Text
        </md-outlined-button>
        <!--?lit$164015876$-->
        <!--?lit$164015876$-->
      </div><hr>
    </div></div><div class="cell code code-has-output" id="cell-a19c257c" tabindex="-1" role="region" aria-label="Cell 5: Code cell: " style="opacity: 1;"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$164015876$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$164015876$--><span class="execution-count"><!--?lit$164015876$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$164015876$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$164015876$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$164015876$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by MD. MINHAZUL ISLAM MINAR 2004095
3:30 PM (31 minutes ago)
executed in 6.801s"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$164015876$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$164015876$-->executed by MD. MINHAZUL ISLAM MINAR 2004095</div><!----><!----><div><!--?lit$164015876$-->3:30 PM (31 minutes ago)</div><!----><!----><div><!--?lit$164015876$-->executed in 6.801s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$164015876$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab colab colab colab colab colab colab colab colab colab colab colab colab colab" data-lang="notebook-python"><span><span class="mtk6">%pip&nbsp;</span><span class="mtk1">install&nbsp;rouge_score</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$164015876$-->Start coding or <span tabindex="0" role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 5 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$--><svg viewBox="0 0 24 24"><!--?lit$164015876$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-4 output_text"><pre>Collecting rouge_score
  Downloading rouge_score-0.1.2.tar.gz (17 kB)
  Preparing metadata (setup.py) ... done
Requirement already satisfied: absl-py in /usr/local/lib/python3.11/dist-packages (from rouge_score) (1.4.0)
Requirement already satisfied: nltk in /usr/local/lib/python3.11/dist-packages (from rouge_score) (3.9.1)
Requirement already satisfied: numpy in /usr/local/lib/python3.11/dist-packages (from rouge_score) (2.0.2)
Requirement already satisfied: six&gt;=1.14.0 in /usr/local/lib/python3.11/dist-packages (from rouge_score) (1.17.0)
Requirement already satisfied: click in /usr/local/lib/python3.11/dist-packages (from nltk-&gt;rouge_score) (8.2.1)
Requirement already satisfied: joblib in /usr/local/lib/python3.11/dist-packages (from nltk-&gt;rouge_score) (1.5.1)
Requirement already satisfied: regex&gt;=2021.8.3 in /usr/local/lib/python3.11/dist-packages (from nltk-&gt;rouge_score) (2024.11.6)
Requirement already satisfied: tqdm in /usr/local/lib/python3.11/dist-packages (from nltk-&gt;rouge_score) (4.67.1)
Building wheels for collected packages: rouge_score
  Building wheel for rouge_score (setup.py) ... done
  Created wheel for rouge_score: filename=rouge_score-0.1.2-py3-none-any.whl size=24934 sha256=773c81febd88ccfa87bcf399794b4381b16ca4b4f8afc928041c8bcaba79fa02
  Stored in directory: /root/.cache/pip/wheels/1e/19/43/8a442dc83660ca25e163e1bd1f89919284ab0d0c1475475148
Successfully built rouge_score
Installing collected packages: rouge_score
Successfully installed rouge_score-0.1.2
</pre></div></div><div></div></colab-static-output-renderer></div></div><div><div></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$164015876$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$164015876$-->Text
        </md-outlined-button>
        <!--?lit$164015876$-->
        <!--?lit$164015876$-->
      </div><hr>
    </div></div><div class="cell code code-has-output focused" id="cell-qkO9TZr3KHuQ" tabindex="-1" role="region" aria-label="Cell 6: Code cell: " style="opacity: 1;"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$164015876$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"><colab-cell-toolbar><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-up-tooltip" data-aria-label="Move cell up
Ctrl+M K" command="move-cell-up" id="button-move-cell-up" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell up
Ctrl+M K">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->arrow_upward</md-icon>
        <!--?lit$164015876$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-up" id="button-move-cell-up-tooltip" message="Move cell up
Ctrl+M K"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Move cell up</div><!----><!----><div><!--?lit$164015876$-->Ctrl+M K</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-down-tooltip" data-aria-label="Move cell down
Ctrl+M J" command="move-cell-down" id="button-move-cell-down" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell down
Ctrl+M J">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->arrow_downward</md-icon>
        <!--?lit$164015876$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-down" id="button-move-cell-down-tooltip" message="Move cell down
Ctrl+M J"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Move cell down</div><!----><!----><div><!--?lit$164015876$-->Ctrl+M J</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----><!--?lit$164015876$--><md-menu positioning="popover" quick="" aria-labelledby="ai-menu-anchor-qkO9TZr3KHuQ" anchor="ai-menu-anchor-qkO9TZr3KHuQ" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$164015876$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$164015876$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$164015876$--><!----><md-menu-item command="generate-code" md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$164015876$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$164015876$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$164015876$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$164015876$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$164015876$-->Generate code</span>
  </md-menu-item><!----><!----><md-menu-item command="explain-cell" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$164015876$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$164015876$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$164015876$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$164015876$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$164015876$-->Explain code</span>
  </md-menu-item><!---->
  </md-menu>
          <md-icon-button touch-target="none" data-aria-haspopup="menu" data-aria-expanded="false" aria-describedby="ai-menu-anchor-qkO9TZr3KHuQ-tooltip" data-aria-label="Available AI features" id="ai-menu-anchor-qkO9TZr3KHuQ" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Available AI features" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
          </md-icon-button>
          <colab-tooltip-trigger aria-hidden="true" for="ai-menu-anchor-qkO9TZr3KHuQ" id="ai-menu-anchor-qkO9TZr3KHuQ-tooltip" message="Available AI features"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Available AI features</div><!----><!--?--></template>
          </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-copy-link-to-cell-tooltip" data-aria-label="Copy link to cell" command="copy-link-to-cell" id="button-copy-link-to-cell" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Copy link to cell">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->link</md-icon>
        <!--?lit$164015876$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-copy-link-to-cell" id="button-copy-link-to-cell-tooltip" message="Copy link to cell"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Copy link to cell</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-add-comment-tooltip" data-aria-label="Add a comment
Ctrl+Alt+M" command="add-comment" id="button-add-comment" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add a comment
Ctrl+Alt+M">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->comment</md-icon>
        <!--?lit$164015876$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-add-comment" id="button-add-comment-tooltip" message="Add a comment
Ctrl+Alt+M"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Add a comment</div><!----><!----><div><!--?lit$164015876$-->Ctrl+Alt+M</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-editor-preferences-tooltip" data-aria-label="Open editor settings" command="editor-preferences" id="button-editor-preferences" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open editor settings">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->settings</md-icon>
        <!--?lit$164015876$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-editor-preferences" id="button-editor-preferences-tooltip" message="Open editor settings"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Open editor settings</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-toggle-edit-markdown-tooltip" data-aria-label="Edit" command="toggle-edit-markdown" id="button-toggle-edit-markdown" toggle="" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Edit" aria-pressed="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->edit</md-icon>
        <!--?lit$164015876$--><md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->edit_off</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-toggle-edit-markdown" id="button-toggle-edit-markdown-tooltip" message="Edit"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Edit</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-mirror-cell-in-tab-tooltip" data-aria-label="Mirror cell in tab" command="mirror-cell-in-tab" id="button-mirror-cell-in-tab" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mirror cell in tab">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$--><svg viewBox="0 0 24 24"><!--?lit$164015876$-->
      <g id="mirror-cell">
        <path d="M4,21V7H2V21a2,2,0,0,0,2,2H18V21Z"></path>
        <path d="M6,13v2H8.6L5,18.6,6.4,20,10,16.4V19h2V13Z"></path>
        <path d="M19,1H8A2,2,0,0,0,6,3v8H8V3H19V17H14v2h5a2,2,0,0,0,2-2V3A2,2,0,0,0,19,1Z"></path>
      </g></svg></md-icon>
        <!--?lit$164015876$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-mirror-cell-in-tab" id="button-mirror-cell-in-tab-tooltip" message="Mirror cell in tab"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Mirror cell in tab</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-delete-cell-or-selection-tooltip" data-aria-label="Delete cell
Ctrl+M D" command="delete-cell-or-selection" id="button-delete-cell-or-selection" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Delete cell
Ctrl+M D">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->delete</md-icon>
        <!--?lit$164015876$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-delete-cell-or-selection" id="button-delete-cell-or-selection-tooltip" message="Delete cell
Ctrl+M D"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Delete cell</div><!----><!----><div><!--?lit$164015876$-->Ctrl+M D</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!--?lit$164015876$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-more-actions-tooltip" data-aria-label="More cell actions" class="cell-toolbar-more" id="button-more-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More cell actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-more-actions" id="button-more-actions-tooltip" message="More cell actions"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->More cell actions</div><!----><!--?--></template>
      </colab-tooltip-trigger><!--?--></template></colab-cell-toolbar></div><div class="main-content" elevation="2"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale focused">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$164015876$--><span class="execution-count"><!--?lit$164015876$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$164015876$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$164015876$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$164015876$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by MD. MINHAZUL ISLAM MINAR 2004095
3:53 PM (44 minutes ago)
executed in 16.378s"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$164015876$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$164015876$-->executed by MD. MINHAZUL ISLAM MINAR 2004095</div><!----><!----><div><!--?lit$164015876$-->3:53 PM (44 minutes ago)</div><!----><!----><div><!--?lit$164015876$-->executed in 16.378s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$164015876$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="47" data-mode-id="notebook-python" style="height: 751px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs" role="code" data-uri="inmemory://model/9" style="width: 1236px; height: 751px;"><div data-mprt="3" class="overflow-guard" style="width: 1236px; height: 751px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 751px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 751px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 751px;"><div style="position:absolute;top:0px;width:100%;height:19px;"></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"></div><div style="position:absolute;top:380px;width:100%;height:19px;"></div><div style="position:absolute;top:399px;width:100%;height:19px;"></div><div style="position:absolute;top:418px;width:100%;height:19px;"></div><div style="position:absolute;top:437px;width:100%;height:19px;"></div><div style="position:absolute;top:456px;width:100%;height:19px;"></div><div style="position:absolute;top:475px;width:100%;height:19px;"></div><div style="position:absolute;top:494px;width:100%;height:19px;"></div><div style="position:absolute;top:513px;width:100%;height:19px;"></div><div style="position:absolute;top:532px;width:100%;height:19px;"></div><div style="position:absolute;top:551px;width:100%;height:19px;"></div><div style="position:absolute;top:570px;width:100%;height:19px;"></div><div style="position:absolute;top:589px;width:100%;height:19px;"></div><div style="position:absolute;top:608px;width:100%;height:19px;"></div><div style="position:absolute;top:627px;width:100%;height:19px;"></div><div style="position:absolute;top:646px;width:100%;height:19px;"></div><div style="position:absolute;top:665px;width:100%;height:19px;"></div><div style="position:absolute;top:684px;width:100%;height:19px;"></div><div style="position:absolute;top:703px;width:100%;height:19px;"></div><div style="position:absolute;top:722px;width:100%;height:19px;"><div class="current-line" style="width:6px; height:19px;"></div></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 1230px; height: 751px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 751px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 1230px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="cslr selected-text top-left-radius top-right-radius bottom-right-radius" style="top:0px;left:0px;width:192px;height:19px;"></div><svg style="position:absolute;width:100px;height:19px" viewBox="0 0 100 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="34.85" cy="9.50" r="1.10"></circle><circle cx="95.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:19px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:177px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius" style="top:0px;left:177px;width:10px;height:19px;"></div><div class="cslr selected-text bottom-right-radius" style="top:0px;left:0px;width:177px;height:19px;"></div><svg style="position:absolute;width:100px;height:19px" viewBox="0 0 100 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="34.85" cy="9.50" r="1.10"></circle><circle cx="95.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:38px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:8px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius" style="top:0px;left:8px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:8px;height:19px;"></div></div><div style="position:absolute;top:57px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:8px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background bottom-left-radius" style="top:0px;left:8px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:8px;height:19px;"></div></div><div style="position:absolute;top:76px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:177px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background bottom-left-radius" style="top:0px;left:177px;width:10px;height:19px;"></div><div class="cslr selected-text top-right-radius" style="top:0px;left:0px;width:177px;height:19px;"></div><svg style="position:absolute;width:154px;height:19px" viewBox="0 0 154 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="49.85" cy="9.50" r="1.10"></circle><circle cx="126.85" cy="9.50" r="1.10"></circle><circle cx="149.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:95px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:262px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background bottom-left-radius" style="top:0px;left:262px;width:10px;height:19px;"></div><div class="cslr selected-text top-right-radius" style="top:0px;left:0px;width:262px;height:19px;"></div><svg style="position:absolute;width:193px;height:19px" viewBox="0 0 193 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="34.85" cy="9.50" r="1.10"></circle><circle cx="134.85" cy="9.50" r="1.10"></circle><circle cx="188.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:114px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:285px;height:19px;"></div><svg style="position:absolute;width:185px;height:19px" viewBox="0 0 185 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="34.85" cy="9.50" r="1.10"></circle><circle cx="126.85" cy="9.50" r="1.10"></circle><circle cx="180.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:133px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:8px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:8px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:8px;height:19px;"></div></div><div style="position:absolute;top:152px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:654px;height:19px;"></div><svg style="position:absolute;width:527px;height:19px" viewBox="0 0 527 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="261.85" cy="9.50" r="1.10"></circle><circle cx="322.85" cy="9.50" r="1.10"></circle><circle cx="391.85" cy="9.50" r="1.10"></circle><circle cx="476.85" cy="9.50" r="1.10"></circle><circle cx="522.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:171px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:8px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:8px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:8px;height:19px;"></div></div><div style="position:absolute;top:190px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:527px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background bottom-left-radius" style="top:0px;left:527px;width:10px;height:19px;"></div><div class="cslr selected-text top-right-radius" style="top:0px;left:0px;width:527px;height:19px;"></div><svg style="position:absolute;width:443px;height:19px" viewBox="0 0 443 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="99.85" cy="9.50" r="1.10"></circle><circle cx="161.85" cy="9.50" r="1.10"></circle><circle cx="230.85" cy="9.50" r="1.10"></circle><circle cx="284.85" cy="9.50" r="1.10"></circle><circle cx="368.85" cy="9.50" r="1.10"></circle><circle cx="407.85" cy="9.50" r="1.10"></circle><circle cx="438.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:209px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:854px;height:19px;"></div><svg style="position:absolute;width:769px;height:19px" viewBox="0 0 769 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="172.85" cy="9.50" r="1.10"></circle><circle cx="234.85" cy="9.50" r="1.10"></circle><circle cx="303.85" cy="9.50" r="1.10"></circle><circle cx="364.85" cy="9.50" r="1.10"></circle><circle cx="395.85" cy="9.50" r="1.10"></circle><circle cx="457.85" cy="9.50" r="1.10"></circle><circle cx="503.85" cy="9.50" r="1.10"></circle><circle cx="580.85" cy="9.50" r="1.10"></circle><circle cx="672.85" cy="9.50" r="1.10"></circle><circle cx="711.85" cy="9.50" r="1.10"></circle><circle cx="734.85" cy="9.50" r="1.10"></circle><circle cx="764.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:228px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:8px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:8px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:8px;height:19px;"></div></div><div style="position:absolute;top:247px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:185px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background bottom-left-radius" style="top:0px;left:185px;width:10px;height:19px;"></div><div class="cslr selected-text top-right-radius" style="top:0px;left:0px;width:185px;height:19px;"></div><svg style="position:absolute;width:139px;height:19px" viewBox="0 0 139 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="49.85" cy="9.50" r="1.10"></circle><circle cx="134.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:266px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:392px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background bottom-left-radius" style="top:0px;left:392px;width:10px;height:19px;"></div><div class="cslr selected-text top-right-radius" style="top:0px;left:0px;width:392px;height:19px;"></div><svg style="position:absolute;width:300px;height:19px" viewBox="0 0 300 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="34.85" cy="9.50" r="1.10"></circle><circle cx="188.85" cy="9.50" r="1.10"></circle><circle cx="295.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:285px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:631px;height:19px;"></div><svg style="position:absolute;width:331px;height:19px" viewBox="0 0 331 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="111.85" cy="9.50" r="1.10"></circle><circle cx="126.85" cy="9.50" r="1.10"></circle><circle cx="326.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:304px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:8px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:8px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:8px;height:19px;"></div></div><div style="position:absolute;top:323px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:100px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background bottom-left-radius" style="top:0px;left:100px;width:10px;height:19px;"></div><div class="cslr selected-text top-right-radius" style="top:0px;left:0px;width:100px;height:19px;"></div><svg style="position:absolute;width:54px;height:19px" viewBox="0 0 54 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="49.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:342px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:635px;height:19px;"></div><svg style="position:absolute;width:543px;height:19px" viewBox="0 0 543 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="80.85" cy="9.50" r="1.10"></circle><circle cx="95.85" cy="9.50" r="1.10"></circle><circle cx="230.85" cy="9.50" r="1.10"></circle><circle cx="276.85" cy="9.50" r="1.10"></circle><circle cx="315.85" cy="9.50" r="1.10"></circle><circle cx="384.85" cy="9.50" r="1.10"></circle><circle cx="438.85" cy="9.50" r="1.10"></circle><circle cx="476.85" cy="9.50" r="1.10"></circle><circle cx="538.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:361px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:8px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:8px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:8px;height:19px;"></div></div><div style="position:absolute;top:380px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:235px;height:19px;"></div><svg style="position:absolute;width:135px;height:19px" viewBox="0 0 135 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="130.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:399px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:146px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:146px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:146px;height:19px;"></div><svg style="position:absolute;width:54px;height:19px" viewBox="0 0 54 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="49.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:418px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:831px;height:19px;"></div><svg style="position:absolute;width:554px;height:19px" viewBox="0 0 554 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="34.85" cy="9.50" r="1.10"></circle><circle cx="41.85" cy="9.50" r="1.10"></circle><circle cx="49.85" cy="9.50" r="1.10"></circle><circle cx="57.85" cy="9.50" r="1.10"></circle><circle cx="118.85" cy="9.50" r="1.10"></circle><circle cx="134.85" cy="9.50" r="1.10"></circle><circle cx="311.85" cy="9.50" r="1.10"></circle><circle cx="434.85" cy="9.50" r="1.10"></circle><circle cx="549.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:437px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:273px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius" style="top:0px;left:273px;width:10px;height:19px;"></div><div class="cslr selected-text bottom-right-radius" style="top:0px;left:0px;width:273px;height:19px;"></div><svg style="position:absolute;width:196px;height:19px" viewBox="0 0 196 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="34.85" cy="9.50" r="1.10"></circle><circle cx="41.85" cy="9.50" r="1.10"></circle><circle cx="49.85" cy="9.50" r="1.10"></circle><circle cx="57.85" cy="9.50" r="1.10"></circle><circle cx="191.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:456px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:215px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius" style="top:0px;left:215px;width:10px;height:19px;"></div><div class="cslr selected-text bottom-right-radius" style="top:0px;left:0px;width:215px;height:19px;"></div><svg style="position:absolute;width:62px;height:19px" viewBox="0 0 62 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="34.85" cy="9.50" r="1.10"></circle><circle cx="41.85" cy="9.50" r="1.10"></circle><circle cx="49.85" cy="9.50" r="1.10"></circle><circle cx="57.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:475px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:8px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:8px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:8px;height:19px;"></div></div><div style="position:absolute;top:494px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:354px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background bottom-left-radius" style="top:0px;left:354px;width:10px;height:19px;"></div><div class="cslr selected-text top-right-radius" style="top:0px;left:0px;width:354px;height:19px;"></div><svg style="position:absolute;width:300px;height:19px" viewBox="0 0 300 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="34.85" cy="9.50" r="1.10"></circle><circle cx="41.85" cy="9.50" r="1.10"></circle><circle cx="49.85" cy="9.50" r="1.10"></circle><circle cx="57.85" cy="9.50" r="1.10"></circle><circle cx="72.85" cy="9.50" r="1.10"></circle><circle cx="188.85" cy="9.50" r="1.10"></circle><circle cx="234.85" cy="9.50" r="1.10"></circle><circle cx="295.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:513px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:554px;height:19px;"></div><svg style="position:absolute;width:416px;height:19px" viewBox="0 0 416 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="34.85" cy="9.50" r="1.10"></circle><circle cx="41.85" cy="9.50" r="1.10"></circle><circle cx="49.85" cy="9.50" r="1.10"></circle><circle cx="57.85" cy="9.50" r="1.10"></circle><circle cx="111.85" cy="9.50" r="1.10"></circle><circle cx="126.85" cy="9.50" r="1.10"></circle><circle cx="411.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:532px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:331px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:331px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:331px;height:19px;"></div><svg style="position:absolute;width:308px;height:19px" viewBox="0 0 308 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="34.85" cy="9.50" r="1.10"></circle><circle cx="41.85" cy="9.50" r="1.10"></circle><circle cx="49.85" cy="9.50" r="1.10"></circle><circle cx="57.85" cy="9.50" r="1.10"></circle><circle cx="134.85" cy="9.50" r="1.10"></circle><circle cx="149.85" cy="9.50" r="1.10"></circle><circle cx="303.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:551px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:677px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background bottom-left-radius" style="top:0px;left:677px;width:10px;height:19px;"></div><div class="cslr selected-text top-right-radius" style="top:0px;left:0px;width:677px;height:19px;"></div><svg style="position:absolute;width:593px;height:19px" viewBox="0 0 593 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="34.85" cy="9.50" r="1.10"></circle><circle cx="41.85" cy="9.50" r="1.10"></circle><circle cx="49.85" cy="9.50" r="1.10"></circle><circle cx="57.85" cy="9.50" r="1.10"></circle><circle cx="111.85" cy="9.50" r="1.10"></circle><circle cx="126.85" cy="9.50" r="1.10"></circle><circle cx="303.85" cy="9.50" r="1.10"></circle><circle cx="495.85" cy="9.50" r="1.10"></circle><circle cx="526.85" cy="9.50" r="1.10"></circle><circle cx="564.85" cy="9.50" r="1.10"></circle><circle cx="588.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:570px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:731px;height:19px;"></div><svg style="position:absolute;width:585px;height:19px" viewBox="0 0 585 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="34.85" cy="9.50" r="1.10"></circle><circle cx="41.85" cy="9.50" r="1.10"></circle><circle cx="49.85" cy="9.50" r="1.10"></circle><circle cx="57.85" cy="9.50" r="1.10"></circle><circle cx="165.85" cy="9.50" r="1.10"></circle><circle cx="180.85" cy="9.50" r="1.10"></circle><circle cx="226.85" cy="9.50" r="1.10"></circle><circle cx="257.85" cy="9.50" r="1.10"></circle><circle cx="280.85" cy="9.50" r="1.10"></circle><circle cx="318.85" cy="9.50" r="1.10"></circle><circle cx="341.85" cy="9.50" r="1.10"></circle><circle cx="488.85" cy="9.50" r="1.10"></circle><circle cx="580.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:589px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:8px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:8px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:8px;height:19px;"></div></div><div style="position:absolute;top:608px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:473px;height:19px;"></div><svg style="position:absolute;width:396px;height:19px" viewBox="0 0 396 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="34.85" cy="9.50" r="1.10"></circle><circle cx="41.85" cy="9.50" r="1.10"></circle><circle cx="49.85" cy="9.50" r="1.10"></circle><circle cx="57.85" cy="9.50" r="1.10"></circle><circle cx="191.85" cy="9.50" r="1.10"></circle><circle cx="222.85" cy="9.50" r="1.10"></circle><circle cx="299.85" cy="9.50" r="1.10"></circle><circle cx="361.85" cy="9.50" r="1.10"></circle><circle cx="391.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:627px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:246px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:246px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:246px;height:19px;"></div><svg style="position:absolute;width:131px;height:19px" viewBox="0 0 131 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="34.85" cy="9.50" r="1.10"></circle><circle cx="41.85" cy="9.50" r="1.10"></circle><circle cx="49.85" cy="9.50" r="1.10"></circle><circle cx="57.85" cy="9.50" r="1.10"></circle><circle cx="88.85" cy="9.50" r="1.10"></circle><circle cx="103.85" cy="9.50" r="1.10"></circle><circle cx="126.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:646px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:354px;height:19px;"></div><svg style="position:absolute;width:216px;height:19px" viewBox="0 0 216 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="34.85" cy="9.50" r="1.10"></circle><circle cx="41.85" cy="9.50" r="1.10"></circle><circle cx="49.85" cy="9.50" r="1.10"></circle><circle cx="57.85" cy="9.50" r="1.10"></circle><circle cx="65.85" cy="9.50" r="1.10"></circle><circle cx="72.85" cy="9.50" r="1.10"></circle><circle cx="80.85" cy="9.50" r="1.10"></circle><circle cx="88.85" cy="9.50" r="1.10"></circle><circle cx="211.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:665px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:8px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:8px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:8px;height:19px;"></div></div><div style="position:absolute;top:684px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:77px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background bottom-left-radius" style="top:0px;left:77px;width:10px;height:19px;"></div><div class="cslr selected-text top-right-radius" style="top:0px;left:0px;width:77px;height:19px;"></div><svg style="position:absolute;width:31px;height:19px" viewBox="0 0 31 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:703px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:415px;height:19px;"></div><svg style="position:absolute;width:316px;height:19px" viewBox="0 0 316 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="3.85" cy="9.50" r="1.10"></circle><circle cx="11.85" cy="9.50" r="1.10"></circle><circle cx="18.85" cy="9.50" r="1.10"></circle><circle cx="26.85" cy="9.50" r="1.10"></circle><circle cx="34.85" cy="9.50" r="1.10"></circle><circle cx="41.85" cy="9.50" r="1.10"></circle><circle cx="49.85" cy="9.50" r="1.10"></circle><circle cx="57.85" cy="9.50" r="1.10"></circle><circle cx="203.85" cy="9.50" r="1.10"></circle><circle cx="249.85" cy="9.50" r="1.10"></circle><circle cx="288.85" cy="9.50" r="1.10"></circle><circle cx="311.85" cy="9.50" r="1.10"></circle></svg></div><div style="position:absolute;top:722px;width:100%;height:19px;"><div class="cslr selected-text bottom-left-radius top-right-radius bottom-right-radius" style="top:0px;left:0px;width:0px;height:19px;"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"><div class="view-ruler" style="width: 2px; height: 751px; left: 615.312px;"></div></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 1230px; height: 751px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk6">%pip&nbsp;</span><span class="mtk1">install&nbsp;rouge_score</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span class="mtk6">%pip&nbsp;</span><span class="mtk1">install&nbsp;streamlit</span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span class="mtk19">import</span><span class="mtk1">&nbsp;streamlit&nbsp;</span><span class="mtk19">as</span><span class="mtk1">&nbsp;st</span></span></div><div style="top:95px;height:19px;" class="view-line"><span><span class="mtk19">from</span><span class="mtk1">&nbsp;transformers&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;pipeline</span></span></div><div style="top:114px;height:19px;" class="view-line"><span><span class="mtk19">from</span><span class="mtk1">&nbsp;rouge_score&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;rouge_scorer</span></span></div><div style="top:133px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:152px;height:19px;" class="view-line"><span><span class="mtk1">st.set_page_config</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">page_title=</span><span class="mtk21">"⚛️&nbsp;PRO-AID&nbsp;Incident&nbsp;Summarizer&nbsp;XAI"</span><span class="mtk1">,&nbsp;page_icon=</span><span class="mtk21">"📝"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:171px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:190px;height:19px;" class="view-line"><span><span class="mtk1">st.title</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"⚛️&nbsp;Nuclear&nbsp;Incident&nbsp;Report&nbsp;Summarizer&nbsp;with&nbsp;XAI&nbsp;</span><span class="mtk21">Insights"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:209px;height:19px;" class="view-line"><span><span class="mtk1">st.markdown</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"Summarize&nbsp;nuclear&nbsp;incident&nbsp;reports&nbsp;and&nbsp;inspect&nbsp;wh</span><span class="mtk21">ich&nbsp;sentences&nbsp;contributed&nbsp;most&nbsp;to&nbsp;the&nbsp;summary."</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:228px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:247px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Load&nbsp;summarizer&nbsp;model</span></span></div><div style="top:266px;height:19px;" class="view-line"><span><span class="mtk19">with</span><span class="mtk1">&nbsp;st.spinner</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"Loading&nbsp;summarization&nbsp;model..."</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1">:</span></span></div><div style="top:285px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;summarizer&nbsp;=&nbsp;pipeline</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"summarization"</span><span class="mtk1">,&nbsp;model=</span><span class="mtk21">"sshleifer/distilbart-cnn-12-6"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:304px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:323px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;User&nbsp;input</span></span></div><div style="top:342px;height:19px;" class="view-line"><span><span class="mtk1">text_input&nbsp;=&nbsp;st.text_area</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"📄&nbsp;Paste&nbsp;your&nbsp;incident&nbsp;report&nbsp;text&nbsp;here:"</span><span class="mtk1">,&nbsp;height=</span><span class="mtk12">300</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:361px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:380px;height:19px;" class="view-line"><span><span class="mtk19">if</span><span class="mtk1">&nbsp;st.button</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"🔍&nbsp;Summarize"</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1">:</span></span></div><div style="top:399px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;text_input:</span></span></div><div style="top:418px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary&nbsp;=&nbsp;summarizer</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">text_input,&nbsp;max_length=</span><span class="mtk12">130</span><span class="mtk1">,&nbsp;min_length=</span><span class="mtk12">40</span><span class="mtk1">,&nbsp;do_sample=</span><span class="mtk6">False</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1 bracket-highlighting-0">[</span><span class="mtk12">0</span><span class="mtk1 bracket-highlighting-0">]</span><span class="mtk1 bracket-highlighting-0">[</span><span class="mtk21">'summary_text'</span><span class="mtk1 bracket-highlighting-0">]</span></span></div><div style="top:437px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.subheader</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"📑&nbsp;Summary"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:456px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.success</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">summary</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:475px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:494px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Explainability&nbsp;using&nbsp;ROUGE-L&nbsp;scores</span></span></div><div style="top:513px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scorer&nbsp;=&nbsp;rouge_scorer.RougeScorer</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk21">'rougeL'</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">,&nbsp;use_stemmer=</span><span class="mtk6">True</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:532px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sentences&nbsp;=&nbsp;text_input.split</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">'.&nbsp;'</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:551px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scores&nbsp;=&nbsp;</span><span class="mtk1 bracket-highlighting-0">[</span><span class="mtk1">scorer.score</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk1">summary,&nbsp;sent</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk21">'rougeL'</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">.fmeasure&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;sent&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;sentences</span><span class="mtk1 bracket-highlighting-0">]</span></span></div><div style="top:570px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;top_sentences&nbsp;=&nbsp;</span><span class="mtk1 bracket-highlighting-0">[</span><span class="mtk1">sent&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;_,&nbsp;sent&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;</span><span class="mtk15">sorted</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk15">zip</span><span class="mtk1 bracket-highlighting-2">(</span><span class="mtk1">scores,&nbsp;sentences</span><span class="mtk1 bracket-highlighting-2">)</span><span class="mtk1">,&nbsp;reverse=</span><span class="mtk6">True</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk1">:</span><span class="mtk12">3</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1 bracket-highlighting-0">]</span></span></div><div style="top:589px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:608px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.subheader</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"🔍&nbsp;Key&nbsp;Sentences&nbsp;Driving&nbsp;the&nbsp;Summary"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:627px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;s&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;top_sentences:</span></span></div><div style="top:646px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.markdown</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk6">f</span><span class="mtk21">"-&nbsp;**</span><span class="mtk1 bracket-highlighting-1">{</span><span class="mtk1">s.strip</span><span class="mtk1 bracket-highlighting-2">(</span><span class="mtk1 bracket-highlighting-2">)</span><span class="mtk1 bracket-highlighting-1">}</span><span class="mtk21">**"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:665px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:684px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">else</span><span class="mtk1">:</span></span></div><div style="top:703px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.warning</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk21">"Please&nbsp;enter&nbsp;text&nbsp;to&nbsp;summarize."</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:722px;height:19px;" class="view-line"><span><span></span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><div class="lightBulbWidget codicon codicon-light-bulb" widgetid="LightBulbWidget" title="Show Code Actions (Ctrl+.)" style="position: absolute; display: none; visibility: hidden; max-width: 1230px;"></div></div><div role="presentation" aria-hidden="true" class="cursors-layer has-selection cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 722px; left: 0px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 1.48148px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 1216px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 1216px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="18" height="1013" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 751px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 751px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 751px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 1236px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3828px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 722px; left: 6px; width: 76914px; height: 1px;"></textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;" class="monaco-editor-background textAreaCover"></div><div data-mprt="4" class="overlayWidgets" style="width: 1236px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 751px;"><div class="minimap-shadow-hidden" style="height: 751px;"></div><canvas width="0" height="1013" style="position: absolute; left: 0px; width: 0px; height: 751px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="1013" style="position: absolute; left: 0px; width: 0px; height: 751px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1361px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 815.76px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 6 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$--><svg viewBox="0 0 24 24"><!--?lit$164015876$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-2 output_text"><pre>Requirement already satisfied: rouge_score in /usr/local/lib/python3.11/dist-packages (0.1.2)
Requirement already satisfied: absl-py in /usr/local/lib/python3.11/dist-packages (from rouge_score) (1.4.0)
Requirement already satisfied: nltk in /usr/local/lib/python3.11/dist-packages (from rouge_score) (3.9.1)
Requirement already satisfied: numpy in /usr/local/lib/python3.11/dist-packages (from rouge_score) (2.0.2)
Requirement already satisfied: six&gt;=1.14.0 in /usr/local/lib/python3.11/dist-packages (from rouge_score) (1.17.0)
Requirement already satisfied: click in /usr/local/lib/python3.11/dist-packages (from nltk-&gt;rouge_score) (8.2.1)
Requirement already satisfied: joblib in /usr/local/lib/python3.11/dist-packages (from nltk-&gt;rouge_score) (1.5.1)
Requirement already satisfied: regex&gt;=2021.8.3 in /usr/local/lib/python3.11/dist-packages (from nltk-&gt;rouge_score) (2024.11.6)
Requirement already satisfied: tqdm in /usr/local/lib/python3.11/dist-packages (from nltk-&gt;rouge_score) (4.67.1)
Requirement already satisfied: streamlit in /usr/local/lib/python3.11/dist-packages (1.45.1)
Requirement already satisfied: altair&lt;6,&gt;=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.0)
Requirement already satisfied: blinker&lt;2,&gt;=1.5.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.9.0)
Requirement already satisfied: cachetools&lt;6,&gt;=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.2)
Requirement already satisfied: click&lt;9,&gt;=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (8.2.1)
Requirement already satisfied: numpy&lt;3,&gt;=1.23 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.0.2)
Requirement already satisfied: packaging&lt;25,&gt;=20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (24.2)
Requirement already satisfied: pandas&lt;3,&gt;=1.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.2.2)
Requirement already satisfied: pillow&lt;12,&gt;=7.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (11.2.1)
Requirement already satisfied: protobuf&lt;7,&gt;=3.20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.29.5)
Requirement already satisfied: pyarrow&gt;=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (18.1.0)
Requirement already satisfied: requests&lt;3,&gt;=2.27 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.32.3)
Requirement already satisfied: tenacity&lt;10,&gt;=8.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (9.1.2)
Requirement already satisfied: toml&lt;2,&gt;=0.10.1 in /usr/local/lib/python3.11/dist-packages (from streamlit) (0.10.2)
Requirement already satisfied: typing-extensions&lt;5,&gt;=4.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.14.0)
Requirement already satisfied: watchdog&lt;7,&gt;=2.1.5 in /usr/local/lib/python3.11/dist-packages (from streamlit) (6.0.0)
Requirement already satisfied: gitpython!=3.1.19,&lt;4,&gt;=3.0.7 in /usr/local/lib/python3.11/dist-packages (from streamlit) (3.1.44)
Requirement already satisfied: pydeck&lt;1,&gt;=0.8.0b4 in /usr/local/lib/python3.11/dist-packages (from streamlit) (0.9.1)
Requirement already satisfied: tornado&lt;7,&gt;=6.0.3 in /usr/local/lib/python3.11/dist-packages (from streamlit) (6.4.2)
Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from altair&lt;6,&gt;=4.0-&gt;streamlit) (3.1.6)
Requirement already satisfied: jsonschema&gt;=3.0 in /usr/local/lib/python3.11/dist-packages (from altair&lt;6,&gt;=4.0-&gt;streamlit) (4.24.0)
Requirement already satisfied: narwhals&gt;=1.14.2 in /usr/local/lib/python3.11/dist-packages (from altair&lt;6,&gt;=4.0-&gt;streamlit) (1.41.0)
Requirement already satisfied: gitdb&lt;5,&gt;=4.0.1 in /usr/local/lib/python3.11/dist-packages (from gitpython!=3.1.19,&lt;4,&gt;=3.0.7-&gt;streamlit) (4.0.12)
Requirement already satisfied: python-dateutil&gt;=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (2.9.0.post0)
Requirement already satisfied: pytz&gt;=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (2025.2)
Requirement already satisfied: tzdata&gt;=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (2025.2)
Requirement already satisfied: charset-normalizer&lt;4,&gt;=2 in /usr/local/lib/python3.11/dist-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (3.4.2)
Requirement already satisfied: idna&lt;4,&gt;=2.5 in /usr/local/lib/python3.11/dist-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (3.10)
Requirement already satisfied: urllib3&lt;3,&gt;=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (2.4.0)
Requirement already satisfied: certifi&gt;=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (2025.4.26)
Requirement already satisfied: smmap&lt;6,&gt;=3.0.1 in /usr/local/lib/python3.11/dist-packages (from gitdb&lt;5,&gt;=4.0.1-&gt;gitpython!=3.1.19,&lt;4,&gt;=3.0.7-&gt;streamlit) (5.0.2)
Requirement already satisfied: MarkupSafe&gt;=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2-&gt;altair&lt;6,&gt;=4.0-&gt;streamlit) (3.0.2)
Requirement already satisfied: attrs&gt;=22.2.0 in /usr/local/lib/python3.11/dist-packages (from jsonschema&gt;=3.0-&gt;altair&lt;6,&gt;=4.0-&gt;streamlit) (25.3.0)
Requirement already satisfied: jsonschema-specifications&gt;=2023.03.6 in /usr/local/lib/python3.11/dist-packages (from jsonschema&gt;=3.0-&gt;altair&lt;6,&gt;=4.0-&gt;streamlit) (2025.4.1)
Requirement already satisfied: referencing&gt;=0.28.4 in /usr/local/lib/python3.11/dist-packages (from jsonschema&gt;=3.0-&gt;altair&lt;6,&gt;=4.0-&gt;streamlit) (0.36.2)
Requirement already satisfied: rpds-py&gt;=0.7.1 in /usr/local/lib/python3.11/dist-packages (from jsonschema&gt;=3.0-&gt;altair&lt;6,&gt;=4.0-&gt;streamlit) (0.25.1)
Requirement already satisfied: six&gt;=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil&gt;=2.8.2-&gt;pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (1.17.0)
</pre></div><div class="stream output-id-26 output_text"><pre>2025-06-16 09:54:04.375 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:54:04.376 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:54:04.377 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:54:04.379 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:54:04.379 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:54:04.381 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:54:04.382 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:54:04.387 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:54:04.898 Thread 'Thread-13': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:54:04.917 Thread 'Thread-13': missing ScriptRunContext! This warning can be ignored when running in bare mode.
Device set to use cpu
2025-06-16 09:54:06.175 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:54:06.177 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:54:06.178 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:54:06.179 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:54:06.180 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:54:06.181 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:54:06.182 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:54:06.185 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:54:06.187 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:54:06.188 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:54:06.189 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:54:06.190 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-16 09:54:06.191 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
</pre></div></div><div></div></colab-static-output-renderer></div></div><div><div></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$164015876$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$164015876$-->Text
        </md-outlined-button>
        <!--?lit$164015876$-->
        <!--?lit$164015876$-->
      </div><hr>
    </div></div><div class="cell code code-has-output" id="cell-HDsmjp5kK3Cy" tabindex="-1" role="region" aria-label="Cell 7: Code cell: " style="opacity: 1;"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$164015876$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$164015876$--><span class="execution-count"><!--?lit$164015876$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$164015876$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$164015876$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$164015876$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by MD. MINHAZUL ISLAM MINAR 2004095
3:59 PM (2 minutes ago)
executed in 0.604s"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$164015876$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$164015876$-->executed by MD. MINHAZUL ISLAM MINAR 2004095</div><!----><!----><div><!--?lit$164015876$-->3:59 PM (2 minutes ago)</div><!----><!----><div><!--?lit$164015876$-->executed in 0.604s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$164015876$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="39" data-mode-id="notebook-python" style="height: 29px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs" role="code" data-uri="inmemory://model/10" style="width: 1236px; height: 29px;"><div data-mprt="3" class="overflow-guard" style="width: 1236px; height: 29px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 29px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 29px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 29px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 1230px; height: 29px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 29px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 1230px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line" style="width:1230px; height:19px;"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 1230px; height: 29px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk6">!</span><span class="mtk1">streamlit&nbsp;run&nbsp;main.py</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><div class="lightBulbWidget codicon codicon-light-bulb" widgetid="LightBulbWidget" title="Show Code Actions (Ctrl+.)" style="position: absolute; display: none; visibility: hidden; max-width: 1230px;"></div></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 0px; left: 169px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 1.48148px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 1216px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 1216px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="18" height="39" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 29px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 29px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 29px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 1236px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3828px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 0px; left: 6px; width: 76914px; height: 1px;"></textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;" class="monaco-editor-background textAreaCover"></div><div data-mprt="4" class="overlayWidgets" style="width: 1236px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 29px;"><div class="minimap-shadow-hidden" style="height: 29px;"></div><canvas width="0" height="39" style="position: absolute; left: 0px; width: 0px; height: 29px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="39" style="position: absolute; left: 0px; width: 0px; height: 29px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1361px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 815.76px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 7 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$--><svg viewBox="0 0 24 24"><!--?lit$164015876$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-1 output_text"><pre>Usage: streamlit run [OPTIONS] TARGET [ARGS]...
Try 'streamlit run --help' for help.

Error: Invalid value: File does not exist: main.py
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$164015876$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$164015876$-->Text
        </md-outlined-button>
        <!--?lit$164015876$-->
        <!--?lit$164015876$-->
      </div><hr>
    </div></div></div>
              </div>
            </div>
          <section class="sidebar" aria-label="Comments" style="display: none;"></section></div>
          <!--?lit$164015876$--> <div class="footer-links" style="padding-bottom: 8px;">
      <a target="_blank" href="https://colab.research.google.com/signup?utm_source=footer&amp;utm_medium=link&amp;utm_campaign=footer_links">
        <!--?lit$164015876$-->Colab paid products
      </a>
      -
      <a href="https://colab.research.google.com/cancel-subscription" target="_blank">
        <!--?lit$164015876$-->Cancel contracts here
      </a>
    </div>
        </div>
      </colab-shaded-scroller>
      <div class="notebook-scroll-shadow" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 4px 4px -2px inset;"></div>
    </div></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer class="sn-resize no-tabs" style="height: 40%"><div class="resizer-thumb"></div>
        <!--?lit$164015876$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$164015876$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      <colab-resizer style="width: 37%" class="we-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$164015876$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$164015876$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$164015876$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      <colab-resizer class="sn-resize no-tabs" style="height: 40%"><div class="resizer-thumb"></div>
        <!--?lit$164015876$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$164015876$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      </colab-resizer>
    </div></colab-tab-layout-container>
        </div>
        <div class="proxies"><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation" src="./main_files/outputframe(3).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./main_files/outputframe(4).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div></div>
      <colab-file-viewer-manager></colab-file-viewer-manager></div>
    <colab-composer view-mode="floating" non-empty-conversation="" hidden=""><template shadowrootmode="open"><!---->
      <colab-composer-conversation><template shadowrootmode="open"><!---->
      <div class="scrollable">
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><!----><colab-composer-message><template shadowrootmode="open"><!----><!--?lit$164015876$--><img class="avatar" data-test-id="user-avatar" src="https://lh3.googleusercontent.com/a/ACg8ocITF1zEYYOhHYICooQT3uKfR1hw1Fie-wzNs_u7b-H3uZk_MQ=s24-mo">
      <div class="body">
        <!--?lit$164015876$--><div class="parts">
      <!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Please explain this error:</div><!---->
    </div> <!--?lit$164015876$-->
      <md-chip-set class="attachments"><template shadowrootmode="open"><!----><slot></slot></template>
        <!--?lit$164015876$--><!---->
      <md-assist-chip has-icon="" class="code" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <div class="container  has-icon ">
        <!--?lit$164015876$-->
      <!--?lit$164015876$--><span class="outline"></span>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$164015876$-->
      <button class="primary action" id="button" type="button"><!--?lit$164015876$-->
      <span class="leading icon" aria-hidden="true">
        <!--?lit$164015876$--><slot name="icon"></slot>
      </span>
      <span class="label">
        <span class="label-text" id="label">
          <!--?lit$164015876$--><slot></slot>
        </span>
      </span>
      <span class="touch"></span>
    </button>
    
    
      </div>
    </template>
        <!--?lit$164015876$--><md-icon slot="icon" class="error-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>error</md-icon> <!--?lit$164015876$--><!--?lit$164015876$--><span style="color: var(--ansi-red);">ModuleNotFoundError</span><span>: No module named 'streamlit'</span><!--?-->
      </md-assist-chip>
    <!---->
      </md-chip-set>
    
        <!--?lit$164015876$--> <!--?lit$164015876$-->
        <!--?lit$164015876$--> <!--?lit$164015876$-->
        <!--?lit$164015876$--> <!--?lit$164015876$-->
      </div></template>
            </colab-composer-message><!----><!----><colab-composer-message><template shadowrootmode="open"><!----><!--?lit$164015876$--><div class="avatar" data-test-id="agent-avatar">
          <!--?lit$164015876$-->
    <svg slot="icon" viewBox="0 -960 960 960" width="24" height="24">
      <defs>
        <lineargradient id="sparkGradient" x1="0" y1="1" x2="1" y2="0">
          <stop offset="33.06%" stop-color="#217BFE"></stop>
          <stop offset="44.4%" stop-color="#078EFB"></stop>
          <stop offset="65.69%" stop-color="#A190FF"></stop>
          <stop offset="75.05%" stop-color="#BD99FE"></stop>
        </lineargradient>
      </defs>
      <path fill="url(#sparkGradient)" d="M480-80q2 0 2-2 0-82 31-154t85-126q54-54 126-85t154-31q2 0 2-2t-2-2q-82 0-154-31t-126-85q-54-54-85-126t-31-154q0-2-2-2t-2 2q0 82-31 154t-85 126q-54 54-126 85T82-482q-2 0-2 2t2 2q82 0 154 31t126 85q54 54 85 126t31 154q0 2 2 2Z"></path>
    </svg>
        </div>
      <div class="body">
        <!--?lit$164015876$--><div class="parts">
      <!--?lit$164015876$--><!----><colab-composer-markdown><template shadowrootmode="open"><!----><div><span><p>The error <code>ModuleNotFoundError: No module named 'streamlit'</code> means that the <code>streamlit</code> library is not installed in your current environment. I'll add a cell to install it.</p>
</span></div></template>
        </colab-composer-markdown><!----><!----><colab-composer-markdown><template shadowrootmode="open"><!----><div><span><p>Great! I've installed the <code>streamlit</code> library. Now you can run the first code cell again to start the Streamlit application. You will see instructions in the output of the cell on how to access the app.</p>
</span></div></template>
        </colab-composer-markdown><!---->
    </div> <!--?lit$164015876$-->
        <!--?lit$164015876$--> <!--?lit$164015876$-->
        <!--?lit$164015876$--> <!--?lit$164015876$-->
        <!--?lit$164015876$--> <!--?lit$164015876$--><colab-ai-rating-buttons rating="unset"><template shadowrootmode="open"><!---->
      <md-icon-button class="thumb-up" toggle="" id="thumbs-up" data-aria-label="Good response" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Good response" aria-pressed="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>thumb_up</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="thumbs-up" message="Good response"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Good response</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <md-icon-button class="thumb-down" toggle="" id="thumbs-down" data-aria-label="Bad response" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Bad response" aria-pressed="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>thumb_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="thumbs-down" message="Bad response"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Bad response</div><!----><!--?--></template>
      </colab-tooltip-trigger>
    </template>
    </colab-ai-rating-buttons>
      </div></template>
            </colab-composer-message><!----><!----><colab-composer-message><template shadowrootmode="open"><!----><!--?lit$164015876$--><img class="avatar" data-test-id="user-avatar" src="https://lh3.googleusercontent.com/a/ACg8ocITF1zEYYOhHYICooQT3uKfR1hw1Fie-wzNs_u7b-H3uZk_MQ=s24-mo">
      <div class="body">
        <!--?lit$164015876$--><div class="parts">
      <!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Please explain this error:</div><!---->
    </div> <!--?lit$164015876$-->
      <md-chip-set class="attachments"><template shadowrootmode="open"><!----><slot></slot></template>
        <!--?lit$164015876$--><!---->
      <md-assist-chip has-icon="" class="code" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <div class="container  has-icon ">
        <!--?lit$164015876$-->
      <!--?lit$164015876$--><span class="outline"></span>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$164015876$-->
      <button class="primary action" id="button" type="button"><!--?lit$164015876$-->
      <span class="leading icon" aria-hidden="true">
        <!--?lit$164015876$--><slot name="icon"></slot>
      </span>
      <span class="label">
        <span class="label-text" id="label">
          <!--?lit$164015876$--><slot></slot>
        </span>
      </span>
      <span class="touch"></span>
    </button>
    
    
      </div>
    </template>
        <!--?lit$164015876$--><md-icon slot="icon" class="error-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>error</md-icon> <!--?lit$164015876$--><!--?lit$164015876$--><span style="color: var(--ansi-red);">ModuleNotFoundError</span><span>: No module named 'rouge_score'</span><!--?-->
      </md-assist-chip>
    <!---->
      </md-chip-set>
    
        <!--?lit$164015876$--> <!--?lit$164015876$-->
        <!--?lit$164015876$--> <!--?lit$164015876$-->
        <!--?lit$164015876$--> <!--?lit$164015876$-->
      </div></template>
            </colab-composer-message><!----><!----><colab-composer-message><template shadowrootmode="open"><!----><!--?lit$164015876$--><div class="avatar" data-test-id="agent-avatar">
          <!--?lit$164015876$-->
    <svg slot="icon" viewBox="0 -960 960 960" width="24" height="24">
      <defs>
        <lineargradient id="sparkGradient" x1="0" y1="1" x2="1" y2="0">
          <stop offset="33.06%" stop-color="#217BFE"></stop>
          <stop offset="44.4%" stop-color="#078EFB"></stop>
          <stop offset="65.69%" stop-color="#A190FF"></stop>
          <stop offset="75.05%" stop-color="#BD99FE"></stop>
        </lineargradient>
      </defs>
      <path fill="url(#sparkGradient)" d="M480-80q2 0 2-2 0-82 31-154t85-126q54-54 126-85t154-31q2 0 2-2t-2-2q-82 0-154-31t-126-85q-54-54-85-126t-31-154q0-2-2-2t-2 2q0 82-31 154t-85 126q-54 54-126 85T82-482q-2 0-2 2t2 2q82 0 154 31t126 85q54 54 85 126t31 154q0 2 2 2Z"></path>
    </svg>
        </div>
      <div class="body">
        <!--?lit$164015876$--><div class="parts">
      <!--?lit$164015876$--><!----><colab-composer-markdown><template shadowrootmode="open"><!----><div><span><p>The error <code>ModuleNotFoundError: No module named 'rouge_score'</code> indicates that the <code>rouge_score</code> library is not installed in your environment. I'll add a cell to install it.</p>
</span></div></template>
        </colab-composer-markdown><!----><!----><colab-composer-markdown><template shadowrootmode="open"><!----><div><span><p>Great! I've installed the <code>rouge_score</code> library. Now you can run the first code cell again to start the Streamlit application. You will see instructions in the output of the cell on how to access the app.</p>
</span></div></template>
        </colab-composer-markdown><!---->
    </div> <!--?lit$164015876$-->
        <!--?lit$164015876$--> <!--?lit$164015876$-->
        <!--?lit$164015876$--> <!--?lit$164015876$-->
        <!--?lit$164015876$--> <!--?lit$164015876$--><colab-ai-rating-buttons rating="unset"><template shadowrootmode="open"><!---->
      <md-icon-button class="thumb-up" toggle="" id="thumbs-up" data-aria-label="Good response" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Good response" aria-pressed="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>thumb_up</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="thumbs-up" message="Good response"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Good response</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <md-icon-button class="thumb-down" toggle="" id="thumbs-down" data-aria-label="Bad response" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Bad response" aria-pressed="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>thumb_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="thumbs-down" message="Bad response"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Bad response</div><!----><!--?--></template>
      </colab-tooltip-trigger>
    </template>
    </colab-ai-rating-buttons>
      </div></template>
            </colab-composer-message><!----><!----><colab-composer-message><template shadowrootmode="open"><!----><!--?lit$164015876$--><img class="avatar" data-test-id="user-avatar" src="https://lh3.googleusercontent.com/a/ACg8ocITF1zEYYOhHYICooQT3uKfR1hw1Fie-wzNs_u7b-H3uZk_MQ=s24-mo">
      <div class="body">
        <!--?lit$164015876$--><div class="parts">
      <!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Please explain this error:</div><!---->
    </div> <!--?lit$164015876$-->
      <md-chip-set class="attachments"><template shadowrootmode="open"><!----><slot></slot></template>
        <!--?lit$164015876$--><!---->
      <md-assist-chip has-icon="" class="code" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <div class="container  has-icon ">
        <!--?lit$164015876$-->
      <!--?lit$164015876$--><span class="outline"></span>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$164015876$-->
      <button class="primary action" id="button" type="button"><!--?lit$164015876$-->
      <span class="leading icon" aria-hidden="true">
        <!--?lit$164015876$--><slot name="icon"></slot>
      </span>
      <span class="label">
        <span class="label-text" id="label">
          <!--?lit$164015876$--><slot></slot>
        </span>
      </span>
      <span class="touch"></span>
    </button>
    
    
      </div>
    </template>
        <!--?lit$164015876$--><md-icon slot="icon" class="error-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>error</md-icon> <!--?lit$164015876$--><!--?lit$164015876$--><span style="color: var(--ansi-red);">SyntaxError</span><span style="color: var(--ansi-red);">:</span><span> invalid syntax</span><!--?-->
      </md-assist-chip>
    <!---->
      </md-chip-set>
    
        <!--?lit$164015876$--> <!--?lit$164015876$-->
        <!--?lit$164015876$--> <!--?lit$164015876$-->
        <!--?lit$164015876$--> <!--?lit$164015876$-->
      </div></template>
            </colab-composer-message><!----><!----><colab-composer-message><template shadowrootmode="open"><!----><!--?lit$164015876$--><div class="avatar" data-test-id="agent-avatar">
          <!--?lit$164015876$-->
    <svg slot="icon" viewBox="0 -960 960 960" width="24" height="24">
      <defs>
        <lineargradient id="sparkGradient" x1="0" y1="1" x2="1" y2="0">
          <stop offset="33.06%" stop-color="#217BFE"></stop>
          <stop offset="44.4%" stop-color="#078EFB"></stop>
          <stop offset="65.69%" stop-color="#A190FF"></stop>
          <stop offset="75.05%" stop-color="#BD99FE"></stop>
        </lineargradient>
      </defs>
      <path fill="url(#sparkGradient)" d="M480-80q2 0 2-2 0-82 31-154t85-126q54-54 126-85t154-31q2 0 2-2t-2-2q-82 0-154-31t-126-85q-54-54-85-126t-31-154q0-2-2-2t-2 2q0 82-31 154t-85 126q-54 54-126 85T82-482q-2 0-2 2t2 2q82 0 154 31t126 85q54 54 85 126t31 154q0 2 2 2Z"></path>
    </svg>
        </div>
      <div class="body">
        <!--?lit$164015876$--><div class="parts">
      <!--?lit$164015876$--><!----><colab-composer-markdown><template shadowrootmode="open"><!----><div><span><p>The error <code>SyntaxError: invalid syntax</code> in cell <code>HDsmjp5kK3Cy</code> is because you are trying to run a shell command (<code>streamlit run main.py</code>) directly in a Python code cell. To execute shell commands in Colab, you need to prefix the command with <code>!</code>. I'll fix the cell by adding the <code>!</code> prefix.</p>
</span></div></template>
        </colab-composer-markdown><!----><!----><colab-composer-markdown><template shadowrootmode="open"><!----><div><span><p>The error <code>Error: Invalid value: File does not exist: main.py</code> means that the <code>streamlit run</code> command could not find a file named <code>main.py</code> to run. You need to create a Python file named <code>main.py</code> in your current directory and put your Streamlit application code inside it. Then, you can run the cell with <code>!streamlit run main.py</code> again.</p>
</span></div></template>
        </colab-composer-markdown><!---->
    </div> <!--?lit$164015876$-->
        <!--?lit$164015876$--> <!--?lit$164015876$-->
        <!--?lit$164015876$--> <!--?lit$164015876$-->
        <!--?lit$164015876$--> <!--?lit$164015876$--><colab-ai-rating-buttons rating="unset"><template shadowrootmode="open"><!---->
      <md-icon-button class="thumb-up" toggle="" id="thumbs-up" data-aria-label="Good response" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Good response" aria-pressed="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>thumb_up</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="thumbs-up" message="Good response"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Good response</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <md-icon-button class="thumb-down" toggle="" id="thumbs-down" data-aria-label="Bad response" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Bad response" aria-pressed="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>thumb_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="thumbs-down" message="Bad response"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Bad response</div><!----><!--?--></template>
      </colab-tooltip-trigger>
    </template>
    </colab-ai-rating-buttons>
      </div></template>
            </colab-composer-message><!---->
      </div>
    </template>
      </colab-composer-conversation>
      <div class="footer">
        <!--?lit$164015876$-->
        <colab-composer-input><template shadowrootmode="open"><!----><div class="wrapper">
        <!--?lit$164015876$-->
        <div class="text-field-and-spark">
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
          <div class="text-field-wrapper" data-value="">
            <md-outlined-text-field type="textarea" rows="1" maxlength="2000" placeholder="What can I help you build?" inputmode="" autocomplete=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <span class="text-field  textarea ">
        <!--?lit$164015876$--><md-outlined-field class="field" count="0" error-text="" label="" max="2000" resizable="" supporting-text=""><template shadowrootmode="open"><!---->
      <div class="field resizable no-label">
        <div class="container-overflow">
          <!--?lit$164015876$-->
          <slot name="container"></slot>
          <!--?lit$164015876$--> <!--?lit$164015876$--> <!--?lit$164015876$-->
      <div class="outline">
        <div class="outline-start"></div>
        <div class="outline-notch">
          <div class="outline-panel-inactive"></div>
          <div class="outline-panel-active"></div>
          <div class="outline-label"><!--?lit$164015876$--></div>
        </div>
        <div class="outline-end"></div>
      </div>
    
          <div class="container">
            <div class="start">
              <slot name="start"></slot>
            </div>
            <div class="middle">
              <div class="label-wrapper">
                <!--?lit$164015876$--> <!--?lit$164015876$-->
              </div>
              <div class="content">
                <slot></slot>
              </div>
            </div>
            <div class="end">
              <slot name="end"></slot>
            </div>
          </div>
        </div>
        <!--?lit$164015876$-->
      <div class="supporting-text"><!--?lit$164015876$--><span><!--?lit$164015876$--></span><!--?lit$164015876$--><span class="counter"><!--?lit$164015876$-->0 / 2000</span></div>
      <slot name="aria-describedby"></slot>
    
      </div>
    </template>
      <!--?lit$164015876$-->
      <span class="icon leading" slot="start">
        <slot name="leading-icon"></slot>
      </span>
    
      <!--?lit$164015876$-->
        <textarea class="input" aria-describedby="description" aria-invalid="false" maxlength="2000" placeholder="What can I help you build?" rows="1" cols="20"></textarea>
      
      <!--?lit$164015876$-->
      <span class="icon trailing" slot="end">
        <slot name="trailing-icon"></slot>
      </span>
    
      <div id="description" slot="aria-describedby" hidden=""><!----><!--?lit$164015876$--> <!--?lit$164015876$-->0 / 2000<!--?--></div>
      <slot name="container" slot="container"></slot>
    </md-outlined-field>
      </span>
    </template>
            </md-outlined-text-field>
          </div>
        </div>
        <div class="actions">
          <!--?lit$164015876$--><md-icon-button id="add-file" data-aria-label="Add files" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add files">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add_circle</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="add-file" message="Add files"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Add files</div><!----><!--?--></template>
      </colab-tooltip-trigger> <!--?lit$164015876$--><md-icon-button id="send" data-aria-label="Send" aria-describedby="send-tooltip" soft-disabled="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Send" aria-disabled="true">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>send</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="send" id="send-tooltip" message="Send"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Send</div><!----><!--?--></template>
      </colab-tooltip-trigger>
        </div>
      </div>
      <!--?lit$164015876$--><!--?--></template></colab-composer-input>
        <!--?lit$164015876$--><div class="legal-notice">
          <!--?lit$164015876$-->Gemini can make mistakes so double-check it and use code with caution.
          <a href="http://g.co/legal/generative-code" target="_blank" aria-label="Learn more Link will open in a new tab">
            <!--?lit$164015876$-->Learn more</a></div> <!--?lit$164015876$-->
      </div>
      <!--?lit$164015876$--><div class="floating-actions">
      <!--?lit$164015876$--><!--?lit$164015876$--><md-icon-button id="close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="close" message="Close"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Close</div><!----><!--?--></template>
      </colab-tooltip-trigger><!--?lit$164015876$-->
      <md-icon-button id="move-to-side-panel" data-aria-label="Move to panel" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move to panel">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>dock_to_left</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="move-to-side-panel" message="Move to panel"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Move to panel</div><!----><!--?--></template>
      </colab-tooltip-trigger>
    <!--?lit$164015876$--><md-icon-button data-aria-haspopup="menu" data-aria-expanded="false" id="more-actions" data-aria-label="More actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="more-actions" message="More actions"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->More actions</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <md-menu positioning="popover" quick="" aria-labelledby="more-actions" anchor="more-actions" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$164015876$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$164015876$--><slot></slot> </div>
        </div>
      </div>
    </template>
        <md-menu-item md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$164015876$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$164015876$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$164015876$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$164015876$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
          <span slot="headline"><!--?lit$164015876$-->New chat</span>
        </md-menu-item>
        <!--?lit$164015876$--><md-menu-item md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$164015876$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$164015876$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$164015876$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$164015876$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
      <span slot="headline"><!--?lit$164015876$-->Send feedback</span>
    </md-menu-item>
      </md-menu><!--?-->
    </div>
    </template></colab-composer><colab-status-bar role="region" aria-label="Runtime status bar" class="status-bar-ui-refresh"><template shadowrootmode="open"><!----><span class="left">
          <slot name="bottom-pane-buttons"></slot>
        </span>
        <span class="middle"><!--?lit$164015876$-->
      <md-icon-button toggle="" id="toggle-composer" data-aria-label="Toggle Gemini" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle Gemini" aria-pressed="false">
        <!--?lit$164015876$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$164015876$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$164015876$--><span class="icon"><slot></slot></span>
        <!--?lit$164015876$-->
        <!--?lit$164015876$--><span class="touch"></span>
  </button></template>
        <!--?lit$164015876$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-composer" message="Toggle Gemini"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Toggle Gemini</div><!----><!--?--></template>
      </colab-tooltip-trigger>
    </span>
        <span class="right">
          <!--?lit$164015876$--><colab-execution-status><template shadowrootmode="open"><!----><md-text-button id="execution-status" aria-describedby="execution-status-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template><!--?lit$164015876$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon><!--?lit$164015876$-->3:59 PM</md-text-button>
      <colab-tooltip-trigger aria-hidden="true" id="execution-status-tooltip" for="execution-status" message="Focus the last run cell

3:59 PM (20 minutes ago)
executed in 0.573s"><template shadowrootmode="open"><!----><!--?lit$164015876$--><!----><div><!--?lit$164015876$-->Focus the last run cell</div><!----><!----><br><!----><!----><div><!--?lit$164015876$-->3:59 PM (20 minutes ago)</div><!----><!----><div><!--?lit$164015876$-->executed in 0.573s</div><!----><!--?--></template>
      </colab-tooltip-trigger></template></colab-execution-status><!--?lit$164015876$--><!--?lit$164015876$--><!--?lit$164015876$--><colab-runtime-status><template shadowrootmode="open"><!----></template></colab-runtime-status>
        </span></template><md-text-button slot="bottom-pane-buttons" command="show-variables" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
        <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->data_object</md-icon>
        <!--?lit$164015876$-->Variables</md-text-button><md-text-button slot="bottom-pane-buttons" command="show-terminal" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
        <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$164015876$-->terminal</md-icon>
        <!--?lit$164015876$-->Terminal</md-text-button></colab-status-bar></div><div class="goog-menu colab-styled-scroller" id="file-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 562.014px; visibility: visible; left: 67.9745px; top: 61.9861px; display: none;"><!--?lit$164015876$--><div command="locate-in-drive" class=" goog-menuitem " role="menuitem" id=":2" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Locate in Drive<!--?lit$164015876$--></div></div><div command="open-in-playground" class=" goog-menuitem " role="menuitem" id=":3" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Open in playground mode<!--?lit$164015876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4" style="user-select: none;"></div><div command="new" class=" goog-menuitem " role="menuitem" id=":5" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->New notebook in Drive<!--?lit$164015876$--></div></div><div command="open" class=" goog-menuitem " role="menuitem" id=":6" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Open notebook<!--?lit$164015876$--><span class="goog-menuitem-accel">Ctrl+O</span></div></div><div command="import-notebook" class=" goog-menuitem " role="menuitem" id=":7" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Upload notebook<!--?lit$164015876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":8" style="user-select: none;"></div><div command="rename" class=" goog-menuitem " role="menuitem" id=":9" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Rename<!--?lit$164015876$--></div></div><div command="move-notebook" class=" goog-menuitem " role="menuitem" id=":a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Move<!--?lit$164015876$--></div></div><div command="trash" class=" goog-menuitem " role="menuitem" id=":b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Move to trash<!--?lit$164015876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":c" style="user-select: none;"></div><div command="clone" class=" goog-menuitem " role="menuitem" id=":d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Save a copy in Drive<!--?lit$164015876$--></div></div><div command="copy-to-gist" class=" goog-menuitem " role="menuitem" id=":e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Save a copy as a GitHub Gist<!--?lit$164015876$--></div></div><div command="copy-to-github" class=" goog-menuitem " role="menuitem" id=":f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Save a copy in GitHub<!--?lit$164015876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":g" style="user-select: none;"></div><div command="save" class=" goog-menuitem " role="menuitem" id=":h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Save<!--?lit$164015876$--><span class="goog-menuitem-accel">Ctrl+S</span></div></div><div command="save-and-checkpoint" class=" goog-menuitem " role="menuitem" id=":i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Save and pin revision<!--?lit$164015876$--><span class="goog-menuitem-accel">Ctrl+M S</span></div></div><div command="show-history" class=" goog-menuitem " role="menuitem" id=":j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Revision history<!--?lit$164015876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":k" style="user-select: none;"></div><div class="goog-submenu goog-menuitem" id="download-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$164015876$-->Download
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div command="print" class=" goog-menuitem " role="menuitem" id=":o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Print<!--?lit$164015876$--><span class="goog-menuitem-accel">Ctrl+P</span></div></div></div><div class="goog-menu" id="download-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$164015876$--><div command="download-ipynb" class=" goog-menuitem " role="menuitem" id=":m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Download .ipynb<!--?lit$164015876$--></div></div><div command="download-python" class=" goog-menuitem " role="menuitem" id=":n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Download .py<!--?lit$164015876$--></div></div></div><div class="goog-menu colab-styled-scroller" id="edit-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 562.014px; visibility: visible; left: 106.748px; top: 61.9861px; display: none;"><!--?lit$164015876$--><div command="undo" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":q" style="user-select: none;" aria-disabled="true"><div class="goog-menuitem-content" style="user-select: none;">Undo<span class="goog-menuitem-accel">Ctrl+M Z</span></div></div><div command="redo" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":r" style="user-select: none;" aria-disabled="true"><div class="goog-menuitem-content" style="user-select: none;">Redo<span class="goog-menuitem-accel">Ctrl+Shift+Y</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":s" style="user-select: none;"></div><div command="select-all" class=" goog-menuitem " role="menuitem" id=":t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Select all cells<!--?lit$164015876$--><span class="goog-menuitem-accel">Ctrl+Shift+A</span></div></div><div command="cut" class=" goog-menuitem " role="menuitem" id=":u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Cut cell or selection<!--?lit$164015876$--></div></div><div command="copy" class=" goog-menuitem " role="menuitem" id=":v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Copy cell or selection<!--?lit$164015876$--></div></div><div command="paste" class=" goog-menuitem " role="menuitem" id=":w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Paste<!--?lit$164015876$--></div></div><div command="delete-cell-or-selection" class=" goog-menuitem " role="menuitem" id=":x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Delete selected cells<!--?lit$164015876$--><span class="goog-menuitem-accel">Ctrl+M D</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":y" style="user-select: none;"></div><div command="find" class=" goog-menuitem " role="menuitem" id=":z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Find and replace<!--?lit$164015876$--><span class="goog-menuitem-accel">Ctrl+H</span></div></div><div command="find-next" class=" goog-menuitem " role="menuitem" id=":10" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Find next<!--?lit$164015876$--><span class="goog-menuitem-accel">Ctrl+G</span></div></div><div command="find-previous" class=" goog-menuitem " role="menuitem" id=":11" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Find previous<!--?lit$164015876$--><span class="goog-menuitem-accel">Ctrl+Shift+G</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":12" style="user-select: none;"></div><div command="notebook-settings" class=" goog-menuitem " role="menuitem" id=":13" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Notebook settings<!--?lit$164015876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":14" style="user-select: none;"></div><div command="clear-outputs" class=" goog-menuitem " role="menuitem" id=":15" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Clear all outputs<!--?lit$164015876$--></div></div></div><div class="goog-menu" id="view-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$164015876$--><div command="show-toc-pane" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":17" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon> </div><!--?lit$164015876$-->Table of contents<!--?lit$164015876$--></div></div><div command="show-fileinfo" class=" goog-menuitem " role="menuitem" id=":18" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Notebook info<!--?lit$164015876$--></div></div><div command="show-executedcode" class=" goog-menuitem " role="menuitem" id=":19" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Executed code history<!--?lit$164015876$--></div></div><div class="goog-submenu goog-menuitem" id="comments-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$164015876$-->Comments
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1e" style="user-select: none;"></div><div command="collapse-sections" class=" goog-menuitem " role="menuitem" id=":1f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Collapse sections<!--?lit$164015876$--></div></div><div command="expand-sections" class=" goog-menuitem " role="menuitem" id=":1g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Expand sections<!--?lit$164015876$--></div></div><div command="save-section-layout" class=" goog-menuitem " role="menuitem" id=":1h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Save collapsed section layout<!--?lit$164015876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1i" style="user-select: none;"></div><div command="hide-code" class=" goog-menuitem " role="menuitem" id=":1j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Show/hide code<!--?lit$164015876$--></div></div><div command="toggle-output" class=" goog-menuitem " role="menuitem" id=":1k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Show/hide output<!--?lit$164015876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1l" style="user-select: none;"></div><div command="focus-next-tab" class=" goog-menuitem " role="menuitem" id=":1m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Focus next tab<!--?lit$164015876$--></div></div><div command="focus-previous-tab" class=" goog-menuitem " role="menuitem" id=":1n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Focus previous tab<!--?lit$164015876$--></div></div><div command="move-tab-to-next" class=" goog-menuitem " role="menuitem" id=":1o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Move tab to next pane<!--?lit$164015876$--></div></div><div command="move-tab-to-prev" class=" goog-menuitem " role="menuitem" id=":1p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Move tab to previous pane<!--?lit$164015876$--></div></div></div><div class="goog-menu" id="comments-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$164015876$--><div command="hide-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Hide comments<!--?lit$164015876$--></div></div><div command="show-minimized-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1c" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Minimize comments<!--?lit$164015876$--></div></div><div command="show-expanded-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Expand comments<!--?lit$164015876$--></div></div></div><div class="goog-menu" id="insert-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$164015876$--><div command="insert-cell-below" class=" goog-menuitem " role="menuitem" id=":1r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Code cell<!--?lit$164015876$--></div></div><div command="add-text" class=" goog-menuitem " role="menuitem" id=":1s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Text cell<!--?lit$164015876$--></div></div><div command="add-section-header" class=" goog-menuitem " role="menuitem" id=":1t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Section header cell<!--?lit$164015876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1u" style="user-select: none;"></div><div command="open-scratch-code-cell" class=" goog-menuitem " role="menuitem" id=":1v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Scratch code cell<!--?lit$164015876$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":1w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Code snippets<!--?lit$164015876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1x" style="user-select: none;"></div><div command="add-form-field" class=" goog-menuitem " role="menuitem" id=":1y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Add a form field<!--?lit$164015876$--></div></div></div><div class="goog-menu" id="runtime-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$164015876$--><div command="runall" class=" goog-menuitem " role="menuitem" id=":20" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Run all<!--?lit$164015876$--></div></div><div command="runbefore" class=" goog-menuitem " role="menuitem" id=":21" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Run before<!--?lit$164015876$--></div></div><div command="runfocused" class=" goog-menuitem " role="menuitem" id=":22" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Run the focused cell<!--?lit$164015876$--></div></div><div command="runselected" class=" goog-menuitem " role="menuitem" id=":23" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Run selection<!--?lit$164015876$--></div></div><div command="runafter" class=" goog-menuitem " role="menuitem" id=":24" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Run cell and below<!--?lit$164015876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":25" style="user-select: none;"></div><div command="interrupt" class=" goog-menuitem " role="menuitem" id=":26" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Interrupt execution<!--?lit$164015876$--></div></div><div command="restart" class=" goog-menuitem " role="menuitem" id=":27" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Restart session<!--?lit$164015876$--></div></div><div command="restart-and-run-all" class=" goog-menuitem " role="menuitem" id=":28" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Restart session and run all<!--?lit$164015876$--></div></div><div command="powerwash-current-vm" class=" goog-menuitem " role="menuitem" id=":29" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Disconnect and delete runtime<!--?lit$164015876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2a" style="user-select: none;"></div><div command="change-runtime-type" class=" goog-menuitem " role="menuitem" id=":2b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Change runtime type<!--?lit$164015876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2c" style="user-select: none;"></div><div command="manage-sessions" class=" goog-menuitem " role="menuitem" id=":2d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Manage sessions<!--?lit$164015876$--></div></div><div command="open-resource-viewer" class=" goog-menuitem " role="menuitem" id=":2e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->View resources<!--?lit$164015876$--></div></div><div command="view-runtime-logs" class=" goog-menuitem " role="menuitem" id=":2f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->View runtime logs<!--?lit$164015876$--></div></div></div><div class="goog-menu" id="tools-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$164015876$--><div command="show-command-palette" class=" goog-menuitem " role="menuitem" id=":2h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Command palette<!--?lit$164015876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2i" style="user-select: none;"></div><div command="preferences" class=" goog-menuitem " role="menuitem" id=":2j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Settings<!--?lit$164015876$--></div></div><div command="shortcuts" class=" goog-menuitem " role="menuitem" id=":2k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Keyboard shortcuts<!--?lit$164015876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2l" style="user-select: none;"></div><div command="open-differ" class=" goog-menuitem " role="menuitem" id=":2m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Diff notebooks<!--?lit$164015876$--> <span class="screenreader-only" style="user-select: none;"><!--?lit$164015876$-->(opens in a new tab)</span></div></div></div><div class="goog-menu" id="help-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$164015876$--><div command="faq" class=" goog-menuitem " role="menuitem" id=":2o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Frequently asked questions<!--?lit$164015876$--></div></div><div command="view-relnotes" class=" goog-menuitem " role="menuitem" id=":2p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->View release notes<!--?lit$164015876$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":2q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Search code snippets<!--?lit$164015876$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2r" style="user-select: none;"></div><div command="report-bug" class=" goog-menuitem " role="menuitem" id=":2s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Report a bug<!--?lit$164015876$--></div></div><div command="report-abuse" class=" goog-menuitem " role="menuitem" id=":2t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Report Drive abuse<!--?lit$164015876$--></div></div><div command="send-feedback" class=" goog-menuitem " role="menuitem" id=":2u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->Send feedback<!--?lit$164015876$--></div></div><div command="view-tos" class=" goog-menuitem " role="menuitem" id=":2v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$164015876$-->View terms of service<!--?lit$164015876$--></div></div></div><dialog class="doc-comments-area" aria-label="Comments"><!----><div class="doc-comments-buttons">
        <md-text-button command="add-comment" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$164015876$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$164015876$--><button id="button" class="button">
      <!--?lit$164015876$-->
      <span class="touch"></span>
      <!--?lit$164015876$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$164015876$-->
    
    </button>
    </template>
          <md-icon slot="icon" filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
          <!--?lit$164015876$-->Add a comment
        </md-text-button>
      </div></dialog><div class="thumbnail"></div><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div><iframe id="apiproxy281d65ffbdb8c750341960e9def7d02a0fe0d9310.656663571" name="apiproxy281d65ffbdb8c750341960e9def7d02a0fe0d9310.656663571" src="./main_files/proxy.html" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px; display: none;"></iframe><div><div>Could not connect to the reCAPTCHA service. Please check your internet connection and reload to get a reCAPTCHA challenge.</div></div><iframe src="./main_files/bscframe.html" style="display: none;"></iframe></body></html>
