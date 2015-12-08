import parametri
import datetime

import sqlite3
connessione = sqlite3.connect('db.sqlite3')

def registra(evento):
    cursore = connessione.cursor()
    cursore.execute("""SELECT impianto_id, operatore_id, ordine_id FROM impianti_pannello WHERE codice=?""", (parametri.codice_pannello,))
    impianto_id, operatore_id, ordine_id = cursore.fetchone()
    cursore.execute("""SELECT quantita_ok, quantita_ko FROM ordini_ordine WHERE id=?""", (ordine_id,))
    quantita_ok, quantita_ko = cursore.fetchone()
    cursore.execute("""INSERT INTO registrazioni_registrazione (istante, evento, impianto_id, operatore_id, ordine_id, quantita_ok, quantita_ko) VALUES (?, ?, ?, ?, ?, ?, ?)""", (datetime.datetime.now(), evento, impianto_id, operatore_id, ordine_id, quantita_ok, quantita_ko,))
    connessione.commit()

def acceso():
    cursore = connessione.cursor()
    cursore.execute("""UPDATE impianti_pannello SET acceso=1 WHERE codice=?""", (parametri.codice_pannello,))
    connessione.commit()
    registra('ON')

def spento():
    cursore = connessione.cursor()
    cursore.execute("""UPDATE impianti_pannello SET acceso=0 WHERE codice=?""", (parametri.codice_pannello,))
    connessione.commit()
    registra('OFF')

def allarmescattato():
    cursore = connessione.cursor()
    cursore.execute("""UPDATE impianti_pannello SET allarme=1 WHERE codice=?""", (parametri.codice_pannello,))
    connessione.commit()
    registra('ALS')

def allarmerientrato():
    cursore = connessione.cursor()
    cursore.execute("""UPDATE impianti_pannello SET allarme=0 WHERE codice=?""", (parametri.codice_pannello,))
    connessione.commit()
    registra('ALR')

def operatoreinserito(tessera):
    cursore = connessione.cursor()
    cursore.execute("""SELECT id FROM operatori_operatore WHERE tessera=?""", (tessera,))
    operatore_id = cursore.fetchone()[0]
    cursore.execute("""UPDATE impianti_pannello SET operatore_id=? WHERE codice=?""", (operatore_id, parametri.codice_pannello,))
    connessione.commit()
    registra('OP+')

def operatoredisinserito(tessera):
    registra('OP-')
    cursore = connessione.cursor()
    cursore.execute("""SELECT id FROM operatori_operatore WHERE tessera=?""", (tessera,))
    operatore_id = cursore.fetchone()[0]
    cursore.execute("""UPDATE impianti_pannello SET operatore_id=NULL WHERE codice=?""", (parametri.codice_pannello,))
    connessione.commit()

def pok():
    cursore = connessione.cursor()
    cursore.execute("""SELECT ordine_id FROM impianti_pannello WHERE codice=?""", (parametri.codice_pannello,))
    ordine_id = cursore.fetchone()[0]
    cursore.execute("""SELECT quantita_ok FROM ordini_ordine WHERE id=?""", (ordine_id,))
    quantita_ok = cursore.fetchone()[0]
    quantita_ok += 1
    cursore.execute("""UPDATE ordini_ordine SET quantita_ok=? WHERE id=?""", (quantita_ok, ordine_id))    
    connessione.commit()

def pko():
    cursore = connessione.cursor()
    cursore.execute("""SELECT ordine_id FROM impianti_pannello WHERE codice=?""", (parametri.codice_pannello,))
    ordine_id = cursore.fetchone()[0]
    cursore.execute("""SELECT quantita_ko FROM ordini_ordine WHERE id=?""", (ordine_id,))
    quantita_ko = cursore.fetchone()[0]
    quantita_ko += 1
    cursore.execute("""UPDATE ordini_ordine SET quantita_ko=? WHERE id=?""", (quantita_ko, ordine_id))    
    connessione.commit()
   
   
#spento()
#acceso()
#allarmescattato()
#allarmerientrato()
#operatoreinserito('0987654321')
#operatoredisinserito('0987654321')
#pok()
#pko()
connessione.close()
