from pathlib import Path
from collections import OrderedDict
import json, zipfile, hashlib, shutil, subprocess, re

ROOT=Path(__file__).resolve().parent.parent
DIST=ROOT/'dist'
GEN=ROOT/'generated_sources'
G1_DIR=ROOT/'translations'/'g1-legacy-forge-3'
MODERN_DIR=ROOT/'translations'/'modern-union'
VERSION='1.0.1'
MODID='catalogue_translation_expansion'
NAME='Catalogue Translation Expansion'
REPO='https://github.com/romaintv20-stee-land-More/catalogue-translation-expansion'
LICENSE=(ROOT/'LICENSE').read_text(encoding='utf-8') if (ROOT/'LICENSE').exists() else 'MIT License'
NOTICE='''Catalogue Translation Expansion\n\nIndependent localization add-on for MrCrayfish Catalogue.\nUpstream: https://github.com/MrCrayfish/Catalogue\nTranslations are AI-assisted and subject to QA/community review.\nLow-confidence locales may intentionally use English fallback.\n'''

EN=OrderedDict([
('fml.menu.mods.filter_updates','Show only mods with updates'),
('catalogue.gui.internal_libraries','Show Internal Libraries'),
('catalogue.gui.no_selection','No mod selected...'),
('catalogue.gui.mod_list','Mods'),
('catalogue.gui.search','Search'),
('catalogue.gui.config','Config'),
('catalogue.gui.website','Website'),
('catalogue.gui.submit_bug','Submit Bug'),
('catalogue.gui.open_mods_folder','Open Mods Folder'),
('catalogue.gui.licenses','License(s): %s'),
('catalogue.gui.authors','Author(s): %s'),
('catalogue.gui.contributors','Contributor(s): %s'),
('catalogue.gui.credits','Credits: %s'),
('catalogue.gui.version','Version: %s'),
('catalogue.gui.update_available','Update: %s'),
('catalogue.gui.info','This menu is provided by Catalogue. Click here to open the CurseForge page for this mod!'),
('catalogue.gui.favourite','Mark as Favorite'),
('catalogue.gui.remove_favourite','Remove as Favorite'),
('catalogue.gui.options','Options'),
('catalogue.gui.filters','Filters'),
('catalogue.gui.filters.configs_only','Mods with Configs'),
('catalogue.gui.filters.updates_only','Mods with Updates'),
('catalogue.gui.filters.favourites','Favorites Only'),
('catalogue.gui.sort','Sort'),
('catalogue.gui.sort.alphabetically','A to Z'),
('catalogue.gui.sort.alphabetically_reverse','Z to A'),
('catalogue.gui.sort.favourites_first','Favorites First'),
('catalogue.gui.hide_libraries','Hide Libraries'),
('catalogue.gui.no_mods','No mods...'),
('catalogue.gui.mod_count','%s Mods'),
('catalogue.gui.library_count','%s Libraries'),
('catalogue.gui.advanced_search.info','Advanced search queries will ignore any active filters'),
('catalogue.gui.show_dependencies','Show Dependencies'),
('catalogue.gui.show_dependents','Show Dependents'),
('catalogue.gui.missing_branding','Missing Branding'),
('catalogue.gui.missing_branding.desc','Are you the author of this mod? Click here for a guide.'),
])
LEGACY_EN=OrderedDict([
('fml.menu.mods.filter_updates','Show only mods with updates'),
('catalogue.gui.no_selection','No mod selected...'),
('catalogue.gui.info','This menu was redesigned by Catalogue. Click here to open the CurseForge page for this mod!'),
])

G1=list(LEGACY_EN)
G2=['catalogue.gui.internal_libraries','catalogue.gui.no_selection','catalogue.gui.mod_list','catalogue.gui.search','catalogue.gui.config','catalogue.gui.open_mods_folder','catalogue.gui.licenses','catalogue.gui.authors','catalogue.gui.contributors','catalogue.gui.version','catalogue.gui.info']
G3=['fml.menu.mods.filter_updates','catalogue.gui.internal_libraries','catalogue.gui.no_selection','catalogue.gui.mod_list','catalogue.gui.search','catalogue.gui.config','catalogue.gui.open_mods_folder','catalogue.gui.licenses','catalogue.gui.authors','catalogue.gui.contributors','catalogue.gui.credits','catalogue.gui.version','catalogue.gui.update_available','catalogue.gui.info']
G4=[k for k in EN if k not in {'fml.menu.mods.filter_updates','catalogue.gui.internal_libraries','catalogue.gui.website','catalogue.gui.submit_bug','catalogue.gui.missing_branding','catalogue.gui.missing_branding.desc'}]
G5=G4[:4]+['catalogue.gui.website','catalogue.gui.submit_bug']+G4[4:]
G6=G5+['catalogue.gui.missing_branding','catalogue.gui.missing_branding.desc']
UNION=list(EN)

legacy_raw='''af_za ar_sa ast_es az_az ba_ru bar be_by bg_bg br_fr brb bs_ba ca_es cs_cz cy_gb da_dk de_at de_ch de_de el_gr en_au en_ca en_gb en_nz en_pt en_ud en_us enp enws eo_uy es_ar es_cl es_ec es_es es_mx es_uy es_ve esan et_ee eu_es fa_ir fi_fi fil_ph fo_fo fr_ca fr_fr fra_de fy_nl ga_ie gd_gb gl_es got_de gv_im haw_us he_il hi_in hr_hr hu_hu hy_am id_id ig_ng io_en is_is it_it ja_jp jbo_en ka_ge kab_kab kk_kz kn_in ko_kr ksh kw_gb la_la lb_lu li_li lol_us lt_lt lv_lv mi_nz mk_mk mn_mn moh_ca ms_my mt_mt nds_de nl_be nl_nl nn_no no_no nuk oc_fr oj_ca ovd pl_pl pt_br pt_pt qya_aa ro_ro ru_ru scn se_no sk_sk sl_si so_so sq_al sr_sp sv_se swg sxu szl ta_in th_th tl_ph tlh_aa tr_tr tt_ru tzl_tzl uk_ua val_es vec_it vi_vn yi_de yo_ng zh_cn zh_tw'''.split()
legacy_excl=set('''bar brb de_at de_ch en_au en_ca en_gb en_nz enp enws es_ar es_cl es_ec es_mx es_uy es_ve esan fr_ca fra_de ksh nl_be nn_no pt_pt swg sxu val_es zh_tw en_pt en_ud lol_us qya_aa tlh_aa tzl_tzl en_us'''.split())
LEGACY=sorted(c for c in legacy_raw if c not in legacy_excl)

current_raw='''af_za ar_sa ast_es az_az ba_ru bar be_by be_latn bg_bg br_fr brb bs_ba ca_es cs_cz cv_cu cy_gb da_dk de_at de_ch de_de deprecated el_gr en_au en_ca en_gb en_nz en_pt en_ud en_us enp enws eo_uy es_ar es_cl es_ec es_es es_mx es_uy es_ve esan et_ee eu_es fa_ir fi_fi fil_ph fo_fo fr_ca fr_ch fr_fr fra_de fur_it fy_nl ga_ie gd_gb gl_es go_fr got_de hal_ua haw_us he_il hi_in hn_no hr_hr hu_hu hy_am id_id ig_ng io_en is_is isv it_it ja_jp jbo_en ka_ge kk_kz kn_in ko_kr ksh kw_gb ky_kg la_la lb_lu li_li lmo lo_la lol_us lt_lt lv_lv lzh mk_mk mn_mn ms_my mt_mt nah nds_de nl_be nl_nl nn_no no_no oc_fr ovd pl_pl pls pt_br pt_pt qcb_es qid qya_aa ro_ro rpr ru_ru ry_ua sah_sah se_no sk_sk sl_si so_so sq_al sr_cs sr_sp sv_se sxu szl ta_in th_th tl_ph tlh_aa tok tr_tr tt_ru tzo_mx uk_ua uz_uz val_es vec_it vi_vn vp_vl vro yi_de yo_ng zh_cn zh_hk zh_tw zlm_arab'''.split()
current_excl=set('''deprecated en_us en_pt en_ud lol_us qya_aa tlh_aa en_au en_ca en_gb en_nz enp enws de_at de_ch es_ar es_cl es_ec es_mx es_uy es_ve esan fr_ca fr_ch nl_be nn_no hn_no pt_pt zh_hk zh_tw be_latn sr_cs qid rpr zlm_arab hal_ua qcb_es bar brb fra_de ksh sxu val_es'''.split())
CURRENT=sorted(c for c in current_raw if c not in current_excl)
MASTER=sorted(set(LEGACY)|set(CURRENT))

def load_json(path):
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=OrderedDict)

def modern_translations():
    return {p.stem:load_json(p) for p in sorted(MODERN_DIR.glob('*.json'))}

def data_for(code, keys, legacy=False):
    if legacy:
        p=G1_DIR/f'{code}.json'
        base=load_json(p) if p.exists() else LEGACY_EN
    else:
        tr=MODERN.get(code, EN)
        base=tr
    source=LEGACY_EN if legacy else EN
    return OrderedDict((k,base.get(k,source[k])) for k in keys)

MODERN=modern_translations()

# Official Catalogue keys protected from needless override.
def protected(target, code):
    p=target.get('protect',{}).get(code)
    if p=='all': return set(target['keys'])
    return set(p or [])

targets=[
 dict(loader='forge',mc='1.16.5',mc_range='[1.16.5,1.16.6)',forge='[36,37)',cat='[1.6.1,1.7)',pack=6,keys=G1,locales=LEGACY,protect={'de_de':'all','it_it':'all'}),
 dict(loader='forge',mc='1.17.1',mc_range='[1.17.1,1.17.2)',forge='[37,38)',cat='[1.5.0,1.6)',pack=7,keys=G1,locales=LEGACY,protect={'de_de':'all','it_it':'all'}),
 dict(loader='forge',mc='1.18.2',mc_range='[1.18.2,1.18.3)',forge='[40,41)',cat='[1.6.1,1.7)',pack=8,keys=G1,locales=LEGACY,protect={c:'all' for c in ['de_de','it_it','pl_pl','zh_cn']}),
 dict(loader='forge',mc='1.19.2',mc_range='[1.19.2,1.19.3)',forge='[43,44)',cat='[1.7.0,1.8)',pack=9,keys=G1,locales=LEGACY,protect={c:'all' for c in ['de_de','it_it','pl_pl','zh_cn']}),
 dict(loader='forge',mc='1.19.3',mc_range='[1.19.3,1.19.4)',forge='[44,45)',cat='[1.7.0,1.8)',pack=12,keys=G1,locales=LEGACY,protect={c:'all' for c in ['de_de','it_it','pl_pl','zh_cn']}),
 dict(loader='forge',mc='1.19.4',mc_range='[1.19.4,1.19.5)',forge='[45,46)',cat='[1.7.1,1.8)',pack=13,keys=G3,locales=MASTER,protect={c:set(G1) for c in ['de_de','it_it','pl_pl','zh_cn']}),
 dict(loader='forge',mc='1.20.1',mc_range='[1.20.1,1.20.2)',forge='[47,48)',cat='[1.8.1,1.9)',pack=15,keys=G3,locales=MASTER,protect={c:set(G1) for c in ['de_de','pl_pl','zh_cn']}),
 dict(loader='forge',mc='1.20.4-1.21.11',mc_range='[1.20.4,1.22)',forge='[49,)',cat='[1.9.1,1.13)',pack=22,supported=[22,64],minf=22,maxf=75,keys=UNION,locales=MASTER,protect={c:set(G1) for c in ['de_de','pl_pl','zh_cn']}),
 dict(loader='fabric',mc='1.19.3',fabric='>=0.14.0',cat='>=1.7.0 <1.8',pack=12,keys=G2,locales=LEGACY,protect={c:'all' for c in ['de_de','it_it','pl_pl','zh_cn']}),
 dict(loader='fabric',mc='1.19.4',fabric='>=0.14.0',cat='>=1.7.1 <1.8',pack=13,keys=G3,locales=MASTER,protect={c:set(G1) for c in ['de_de','it_it','pl_pl','zh_cn']}),
 dict(loader='fabric',mc='1.20.1',fabric='>=0.14.0',cat='>=1.8.1 <1.9',pack=15,keys=G3,locales=MASTER,protect={c:set(G1) for c in ['de_de','pl_pl','zh_cn']}),
 dict(loader='fabric',mc='1.20.4-26.2',fabric='>=0.15.3',cat='>=1.9.1 <1.13',pack=22,supported=[22,64],minf=22,maxf=88,keys=UNION,locales=MASTER,protect={c:set(G1) for c in ['de_de','pl_pl','zh_cn']}),
 dict(loader='neoforge',mc='1.20.4-26.2',neo='[20.4,27)',cat='[1.9.1,1.13)',pack=22,supported=[22,64],minf=22,maxf=88,keys=UNION,locales=MASTER,protect={c:set(G1) for c in ['de_de','pl_pl','zh_cn']}),
]

def pack_mcmeta(t):
    p={'description':f'{NAME} {VERSION}','pack_format':t['pack']}
    if 'supported' in t: p['supported_formats']=t['supported']
    if 'minf' in t: p['min_format']=t['minf']; p['max_format']=t['maxf']
    return json.dumps({'pack':p},ensure_ascii=False,indent=2)+'\n'

def forge_toml(t):
    return f'''modLoader="javafml"\nloaderVersion="{t['forge']}"\nlicense="MIT"\nissueTrackerURL="{REPO}/issues"\n\n[[mods]]\nmodId="{MODID}"\nversion="{VERSION}"\ndisplayName="{NAME}"\nauthors="romaintv20-stee-land-More"\ndisplayURL="{REPO}"\ndescription=''' + "'''Translations for Catalogue across Minecraft versions and loaders.'''\n" + f'''\n[[dependencies.{MODID}]]\nmodId="forge"\nmandatory=true\nversionRange="{t['forge']}"\nordering="NONE"\nside="BOTH"\n\n[[dependencies.{MODID}]]\nmodId="minecraft"\nmandatory=true\nversionRange="{t['mc_range']}"\nordering="NONE"\nside="BOTH"\n\n[[dependencies.{MODID}]]\nmodId="catalogue"\nmandatory=true\nversionRange="{t['cat']}"\nordering="AFTER"\nside="CLIENT"\n'''

def fabric_json(t):
    mc='>=1.20.4 <=26.2' if t['mc']=='1.20.4-26.2' else t['mc']
    return json.dumps({'schemaVersion':1,'id':MODID,'version':VERSION,'name':NAME,'description':'Translations for Catalogue across Minecraft versions.','authors':['romaintv20-stee-land-More'],'contact':{'sources':REPO,'issues':REPO+'/issues'},'license':'MIT','environment':'client','depends':{'fabricloader':t['fabric'],'minecraft':mc,'catalogue':t['cat']}},indent=2,ensure_ascii=False)+'\n'

def neo_toml(t):
    return f'''modLoader = "javafml"\nloaderVersion = "[2,)"\nlicense = "MIT"\nissueTrackerURL = "{REPO}/issues"\n\n[[mods]]\nmodId = "{MODID}"\nversion = "{VERSION}"\ndisplayName = "{NAME}"\nauthors = "romaintv20-stee-land-More"\ndescription = "Translations for Catalogue across Minecraft versions."\n\n[[dependencies.{MODID}]]\nmodId = "neoforge"\ntype = "required"\nversionRange = "{t['neo']}"\nordering = "NONE"\nside = "BOTH"\n\n[[dependencies.{MODID}]]\nmodId = "minecraft"\ntype = "required"\nversionRange = "[1.20.4,27)"\nordering = "NONE"\nside = "BOTH"\n\n[[dependencies.{MODID}]]\nmodId = "catalogue"\ntype = "required"\nversionRange = "{t['cat']}"\nordering = "AFTER"\nside = "CLIENT"\n'''

def build_stubs():
    work=ROOT/'.build_stubs'; shutil.rmtree(work,ignore_errors=True)
    def one(name,pkg,release):
        src=work/name/'src'; out=work/name/'out'; ann=src/Path(*pkg.split('.')); mod=src/'com/romaintv/cataloguetranslationexpansion'
        ann.mkdir(parents=True); mod.mkdir(parents=True); out.mkdir(parents=True)
        (ann/'Mod.java').write_text(f'package {pkg};\nimport java.lang.annotation.*;\n@Retention(RetentionPolicy.RUNTIME)\n@Target(ElementType.TYPE)\npublic @interface Mod {{ String value(); }}\n',encoding='utf-8')
        (mod/'CatalogueTranslationExpansion.java').write_text(f'package com.romaintv.cataloguetranslationexpansion;\nimport {pkg}.Mod;\n@Mod("{MODID}")\npublic final class CatalogueTranslationExpansion {{ public CatalogueTranslationExpansion() {{}} }}\n',encoding='utf-8')
        try: subprocess.run(['javac','--release',str(release),'-d',str(out),str(ann/'Mod.java'),str(mod/'CatalogueTranslationExpansion.java')],check=True,capture_output=True,text=True)
        except FileNotFoundError as e: raise RuntimeError('javac not found; install JDK 21+') from e
        except subprocess.CalledProcessError as e: raise RuntimeError(e.stderr) from e
        return out/'com/romaintv/cataloguetranslationexpansion/CatalogueTranslationExpansion.class'
    return one('forge','net.minecraftforge.fml.common',8), one('neoforge','net.neoforged.fml.common',17)

def validate_sources():
    assert len(LEGACY)==91 and len(CURRENT)==101 and len(MASTER)==108
    assert len(MODERN)==50
    for code,data in MODERN.items():
        if set(data)!=set(EN): raise ValueError(f'{code}: modern union keys differ from EN')
        for k,v in data.items():
            if EN[k].count('%s')!=v.count('%s'): raise ValueError(f'{code}: placeholder mismatch {k}')
    for p in G1_DIR.glob('*.json'):
        d=load_json(p)
        if set(d)!=set(G1): raise ValueError(f'{p.name}: G1 key mismatch')
        for k,v in d.items():
            if LEGACY_EN[k].count('%s')!=v.count('%s'): raise ValueError(f'{p.name}: placeholder mismatch {k}')

def write_generated():
    shutil.rmtree(GEN,ignore_errors=True); GEN.mkdir()
    for name,keys,legacy in [('g1',G1,True),('g2',G2,False),('g3',G3,False),('g4',G4,False),('g5',G5,False),('g6',G6,False)]:
        d=GEN/name; d.mkdir()
        src=LEGACY_EN if legacy else EN
        (d/'en_us.json').write_text(json.dumps(OrderedDict((k,src[k]) for k in keys),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        for code in MASTER:
            (d/f'{code}.json').write_text(json.dumps(data_for(code,keys,legacy),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def build():
    validate_sources(); write_generated(); shutil.rmtree(DIST,ignore_errors=True); DIST.mkdir()
    forge_cls,neo_cls=build_stubs(); report=[]
    for t in targets:
        fn=f'CatalogueTranslationExpansion-{VERSION}-{t["loader"]}-mc{t["mc"]}.jar'; path=DIST/fn
        with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
            z.writestr('META-INF/MANIFEST.MF',f'Manifest-Version: 1.0\nImplementation-Title: {NAME}\nImplementation-Version: {VERSION}\n\n')
            z.writestr('pack.mcmeta',pack_mcmeta(t)); z.writestr('META-INF/LICENSE.txt',LICENSE); z.writestr('META-INF/THIRD_PARTY_NOTICES.txt',NOTICE)
            if t['loader']=='forge': z.writestr('META-INF/mods.toml',forge_toml(t)); z.write(forge_cls,'com/romaintv/cataloguetranslationexpansion/CatalogueTranslationExpansion.class')
            elif t['loader']=='fabric': z.writestr('fabric.mod.json',fabric_json(t))
            else: z.writestr('META-INF/mods.toml',neo_toml(t)); z.writestr('META-INF/neoforge.mods.toml',neo_toml(t)); z.write(neo_cls,'com/romaintv/cataloguetranslationexpansion/CatalogueTranslationExpansion.class')
            count=0
            for code in t['locales']:
                vals=data_for(code,t['keys'],legacy=(t['keys'] is G1)); prot=protected(t,code)
                vals=OrderedDict((k,v) for k,v in vals.items() if k not in prot)
                if vals:
                    z.writestr(f'assets/catalogue/lang/{code}.json',json.dumps(vals,ensure_ascii=False,indent=2)+'\n'); count+=1
        report.append({'file':fn,'loader':t['loader'],'minecraft':t['mc'],'language_files':count,'size':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    (DIST/'build-report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    (DIST/'SHA256SUMS.txt').write_text(''.join(f"{r['sha256']}  {r['file']}\n" for r in report),encoding='utf-8')
    bundle=DIST/f'CatalogueTranslationExpansion-{VERSION}-ALL-JARS.zip'
    with zipfile.ZipFile(bundle,'w',zipfile.ZIP_DEFLATED) as z:
        for r in report: z.write(DIST/r['file'],r['file'])
        z.write(DIST/'SHA256SUMS.txt','SHA256SUMS.txt'); z.write(DIST/'build-report.json','build-report.json')
    qa(report); return report,bundle

def qa(report):
    assert len(report)==13
    for r in report:
        with zipfile.ZipFile(DIST/r['file']) as z:
            names=z.namelist(); assert 'pack.mcmeta' in names; json.loads(z.read('pack.mcmeta'))
            langs=[n for n in names if n.startswith('assets/catalogue/lang/') and n.endswith('.json')]; assert langs
            for n in langs: json.loads(z.read(n).decode('utf-8'))
            if r['loader']=='forge': assert 'META-INF/mods.toml' in names and any(n.endswith('.class') for n in names)
            elif r['loader']=='fabric': assert 'fabric.mod.json' in names; json.loads(z.read('fabric.mod.json'))
            else: assert 'META-INF/mods.toml' in names and 'META-INF/neoforge.mods.toml' in names and any(n.endswith('.class') for n in names)

if __name__=='__main__':
    report,bundle=build()
    print(f'QA OK: {len(report)} JARs; LEGACY={len(LEGACY)} CURRENT={len(CURRENT)} MASTER={len(MASTER)} FULL_TRANSLATED={len(MODERN)}')
    for r in report: print(f"{r['file']} | {r['language_files']} language files | {r['sha256'][:12]}")
    print('BUNDLE',bundle)
