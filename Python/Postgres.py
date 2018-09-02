#!/usr/bin/env python
# -*- coding: utf-8 -*-
# title           :menu.py
# description     :This program displays an interactive menu on CLI
# author          :
# date            :
# version         :0.1
# usage           :python menu.py
# notes           :
# python_version  :3.6.5
# =======================================================================

# Import the modules needed to run the script.
import sys, os
import getch
import psycopg2

# Main definition - constants
menu_actions = {}

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system('clear')
    #    print "Welcome,\n"
    #    print "Please choose the menu you want to start:"
    print (30 * '-')
    print ("   M A I N - M E N U ")
    print (30 * '-')
    print ("1. Oracle")
    print ("2. Sql Server")
    print ("3. Postgres")
    print ("4. Mysql")
    print ("0. Quit")
    print ("\n")
    choice = input(" Select Option :   ")
    exec_menu(choice)

    return


# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return

# Menu 1
def OracleConfiguration():
    print ("Oracle \n")
    return

# Menu 2
def SQLServerConfiguration():
    print ("SQL Server !\n")
    return

# Menu 3
def postgresConfiguration():
    """
            Function to get the postgres connection details

        """
    global conn
    global db_version
    try:
        print (30 * '-')
        print ("   Postgres Server Details/Credentials")
        print (30 * '-')
        #dbserverip = input("DB Server IP : ")
        #dbport     = input("DB Server Port : ")
        #dbdatabase = input("Database Name : ")
        #dbusername = input("DB Username : ")
        #dbpassword = input("DB Password : ")

        # create connection using the above Parameter

        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="zantaz")
        cur = conn.cursor()
        cur.execute("SELECT setting FROM pg_settings WHERE name = 'server_version'")

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        
       # close the communication with the PostgreSQL
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    postgresmenu()
    
    
#Postgres Sub Menu
def postgresmenu():
    os.system('clear')
    print (30 * '-')
    print ("   Select the Task to Perform     ")
    print (30 * '-')
    print ("1. No. of Connections")
    print ("2. No. of Idle Connections")
    print ("3. Postgres Status")
    print ("4. Bloating Ratio")
    print ("5. Blocking/Locks")
    print ("6. Print Database Configuration")
    print ("7. Replication Status")
    print ("8. Other Maintenance")
    print ("9. PgPool")
    print ("0. Quit")
    print ("\n")
    choice = input(" Select Menu: ")
    exec_postgresaction(choice)
    return

def databasemainteiancetasks():
    os.system('clear')
    print (30 * '-')
    print ("   Other Database Tasks     ")
    print (30 * '-')
    print ("1. VACUUM - Database")
    print ("2. VACUUM - Table")
    print ("3. Backup - Database")
    print ("4. Backup - Table")
    print ("5. Database Re-sync")
    print ("6. Database Analyze")
    print ("9. Main Menu")
    print ("\n")
    choice = input(" Select Menu: ")
    exec_databasemainteiancetasks(choice)
    return
    
def pgpoolMenu():
    os.system('clear')
    print (30 * '-')
    print ("   Pgpool      ")
    print (30 * '-')
    print ("1. Pgpool Status")
    print ("2. No. Pgpool Connection")
    print ("3. Node Status")
    print ("4. Node Re-sync")
    print ("6. Main Menu")
    print ("\n")
    choice = input(" Select Menu: ")
    exec_pgpoolMenu(choice)
    return


    
# Menu 4
def MysqlConfiguration():
    print ("MYSQL !\n")
    return


# Back to main menu
def back():
    menu_actions['main_menu']()


# Exit program
def exit():
    sys.exit()

# Execute menu

def exec_pgpoolMenu(choice):
    """
            Function to connect to the Server using VIP

    """
    global pgconn
    #os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_pgpoolactions['pgpoolMenu']()
    else:
        try:
            # print (30 * '-')
            # print ("  Pgpool Connection Details")
            # print (30 * '-')
            # dbserverip = input("DB Server IP : ")
            # dbport     = input("DB Server Port : ")
            # dbdatabase = input("Database Name : ")
            # dbusername = input("DB Username : ")
            # dbpassword = input("DB Password : ")
    
            # create connection using the above Parameter

            pgconn = psycopg2.connect(host="16.144.132.46", database="postgres", user="postgres", password="zantaz",
                                     port="9999")
            # cur1 = pgconn.cursor()
            # cur1.execute("SELECT setting FROM pg_settings WHERE name = 'server_version'")
    
            # display the PostgreSQL database server version
            #Replication_version = cur1.fetchone()
            # print (Replication_version)
            # close the communication with the PostgreSQL
            # cur1.close()
            
            menu_pgpoolactions[ch]()
        except KeyError:
            print ("Invalid selection, please try again.\n")
            menu_actions['pgpoolMenu']()
    return

def exec_postgresaction(choice):
    #os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_postgresactions['postgresmenu']()
    else:
        try:
            menu_postgresactions[ch]()
        except KeyError:
            print ("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return

def exec_databasemainteiancetasks(choice):
    #os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_databasemainteiancetasks['mnuOtherpgmainteiance']()
    else:
        try:
            menu_databasemainteiancetasks[ch]()
        except KeyError:
            print ("Invalid selection, please try again.\n")
            menu_actions['mnuOtherpgmainteiance']()
    return


#Postgres Related Functions


def noofconnections():
    # os.system('clear')
    """
    Display the no of Connections
    
    """
    try:
        print (30 * '-')
        print (" Active Connections ")
        print (30 * '-')
        cur = conn.cursor()

        cur.execute ("SELECT datid,datname,pid,usesysid,usename from pg_stat_activity  where state = 'active'")
        row = cur.fetchone()

        while row is not None:
                    print(row)
                    row = cur.fetchone()
        print("Press any key")
        char = getch.getch()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    postgresmenu()


def noofidleconnections():
    # os.system('clear')
    """
    Display the no of Connections
    """
    try:
        print (30 * '-')
        print ("   Idle Connections     ")
        print (30 * '-')
        cur = conn.cursor()
        cur.execute("SELECT datid,datname,pid,usesysid,usename from pg_stat_activity  where state = 'idle'")
        row = cur.fetchone()
        
        while row is not None:
            print(row)
            row = cur.fetchone()
        print("Press any key")
        char = getch.getch()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    postgresmenu()

def printdatabaseconfiguration():
    # os.system('clear')
    """
    Print the Database Configuration
    
    """
    try:
        print (30 * '-')
        print ("   Database Configuration Parameters + Values   ")
        print (30 * '-')
        cur = conn.cursor()

        cur.execute ('SELECT name, setting, unit from pg_settings')
        row = cur.fetchone()
        while row is not None:
            print(row)
            #print ("{}     |     {}     |    {} ".format(row))
            row = cur.fetchone()
        
        print("Press any key")
        char = getch.getch()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error =" , error)
    postgresmenu()




def pgblocking():
    # os.system('clear')
    """
    Fucntion is to list the pids which are are blocking SQL statements (these only find row-level locks, not object-level locks).
    
    """
    try:
        print (30 * '-')
        print ("  Block/Lock Report   ")
        print (30 * '-')
        cur = conn.cursor()
        cur.execute ('SELECT blocked_locks.pid AS blocked_pid, blocked_activity.usename  AS blocked_user, blocking_locks.pid AS blocking_pid, blocking_activity.usename AS blocking_user, blocked_activity.query AS blocked_statement,  blocking_activity.query   AS current_statement_in_blocking_process FROM  pg_catalog.pg_locks blocked_locks JOIN pg_catalog.pg_stat_activity blocked_activity  ON blocked_activity.pid = blocked_locks.pid JOIN pg_catalog.pg_locks blocking_locks  ON blocking_locks.locktype = blocked_locks.locktype AND blocking_locks.DATABASE IS NOT DISTINCT FROM blocked_locks.DATABASE AND blocking_locks.relation IS NOT DISTINCT FROM blocked_locks.relation AND blocking_locks.page IS NOT DISTINCT FROM blocked_locks.page AND blocking_locks.tuple IS NOT DISTINCT FROM blocked_locks.tuple AND blocking_locks.virtualxid IS NOT DISTINCT FROM blocked_locks.virtualxid AND blocking_locks.transactionid IS NOT DISTINCT FROM blocked_locks.transactionid AND blocking_locks.classid IS NOT DISTINCT FROM blocked_locks.classid AND blocking_locks.objid IS NOT DISTINCT FROM blocked_locks.objid AND blocking_locks.objsubid IS NOT DISTINCT FROM blocked_locks.objsubid AND blocking_locks.pid != blocked_locks.pid JOIN pg_catalog.pg_stat_activity blocking_activity ON blocking_activity.pid = blocking_locks.pid WHERE NOT blocked_locks.GRANTED')
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()
            
        print("Press any key")
        char = getch.getch()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    postgresmenu()

## The following fucntion is to see what processes are blocking SQL statements (these only find row-level locks, not object-level locks).


def pgbloating():
    # os.system('clear')
    try:
        print (30 * '-')
        print ("   Bloating Report  - Table ")
        print (30 * '-')
        cur = conn.cursor()
        sql = " WITH constants AS ( "
        sql += " SELECT current_setting('block_size')::numeric AS bs, 23 AS hdr, 8 AS ma"
        sql += " ),"
        sql += " no_stats AS ( "
        sql += " SELECT table_schema, table_name,"
        sql += " n_live_tup::numeric as est_rows,"
        sql += " pg_table_size(relid)::numeric as table_size "
        sql += " FROM information_schema.columns "
        sql += " JOIN pg_stat_user_tables as psut "
        sql += " ON table_schema = psut.schemaname "
        sql += " AND table_name = psut.relname "
        sql += " LEFT OUTER JOIN pg_stats "
        sql += " ON table_schema = pg_stats.schemaname "
        sql += " AND table_name = pg_stats.tablename "
        sql += " AND column_name = attname "
        sql += " WHERE attname IS NULL "
        sql += " AND table_schema NOT IN ('pg_catalog', 'information_schema') "
        sql += " GROUP BY table_schema, table_name, relid, n_live_tup "
        sql += " ), "
        sql += " null_headers AS ( "
        sql += " SELECT "
        sql += " hdr+1+(sum(case when null_frac <> 0 THEN 1 else 0 END)/8) as nullhdr, "
        sql += " SUM((1-null_frac)*avg_width) as datawidth, "
        sql += " MAX(null_frac) as maxfracsum, "
        sql += " schemaname, "
        sql += " tablename, "
        sql += " hdr, ma, bs "
        sql += " FROM pg_stats CROSS JOIN constants "
        sql += " LEFT OUTER JOIN no_stats "
        sql += "    ON schemaname = no_stats.table_schema "
        sql += "    AND tablename = no_stats.table_name "
        sql += " WHERE schemaname NOT IN ('pg_catalog', 'information_schema') "
        sql += " AND no_stats.table_name IS NULL "
        sql += " AND EXISTS ( SELECT 1 "
        sql += "    FROM information_schema.columns "
        sql += "        WHERE schemaname = columns.table_schema "
        sql += "            AND tablename = columns.table_name ) "
        sql += " GROUP BY schemaname, tablename, hdr, ma, bs "
        sql += " ), "
        sql += " data_headers AS ( "
        sql += " SELECT "
        sql += " ma, bs, hdr, schemaname, tablename, "
        sql += " (datawidth+(hdr+ma-(case when hdr%ma=0 THEN ma ELSE hdr%ma END)))::numeric AS datahdr, "
        sql += " (maxfracsum*(nullhdr+ma-(case when nullhdr%ma=0 THEN ma ELSE nullhdr%ma END))) AS nullhdr2 "
        sql += " FROM null_headers "
        sql += " ), "
        sql += " table_estimates AS ( "
        sql += " SELECT schemaname, tablename, bs, "
        sql += " reltuples::numeric as est_rows, relpages * bs as table_bytes, "
        sql += " CEIL((reltuples* "
        sql += "    (datahdr + nullhdr2 + 4 + ma - "
        sql += "        (CASE WHEN datahdr%ma=0 "
        sql += "            THEN ma ELSE datahdr%ma END) "
        sql += "        )/(bs-20))) * bs AS expected_bytes, "
        sql += " reltoastrelid "
        sql += " FROM data_headers "
        sql += " JOIN pg_class ON tablename = relname "
        sql += " JOIN pg_namespace ON relnamespace = pg_namespace.oid "
        sql += "    AND schemaname = nspname "
        sql += " WHERE pg_class.relkind = 'r' "
        sql += " ), "
        sql += " estimates_with_toast AS ( "
        sql += " SELECT schemaname, tablename, "
        sql += " TRUE as can_estimate, "
        sql += " est_rows, "
        sql += " table_bytes + ( coalesce(toast.relpages, 0) * bs ) as table_bytes, "
        sql += " expected_bytes + ( ceil( coalesce(toast.reltuples, 0) / 4 ) * bs ) as expected_bytes "
        sql += " FROM table_estimates LEFT OUTER JOIN pg_class as toast "
        sql += " ON table_estimates.reltoastrelid = toast.oid "
        sql += "             AND toast.relkind = 't' "
        sql += " ), "
        sql += " table_estimates_plus AS ( "
        sql += " SELECT current_database() as databasename, "
        sql += "             schemaname, tablename, can_estimate, "
        sql += "             est_rows, "
        sql += "             CASE WHEN table_bytes > 0 "
        sql += "                 THEN table_bytes::NUMERIC "
        sql += "                 ELSE NULL::NUMERIC END "
        sql += "                 AS table_bytes, "
        sql += "             CASE WHEN expected_bytes > 0 "
        sql += "                 THEN expected_bytes::NUMERIC "
        sql += "                 ELSE NULL::NUMERIC END "
        sql += "            AS expected_bytes, "
        sql += "             CASE WHEN expected_bytes > 0 AND table_bytes > 0 "
        sql += "                 AND expected_bytes <= table_bytes "
        sql += "                 THEN (table_bytes - expected_bytes)::NUMERIC "
        sql += "                 ELSE 0::NUMERIC END AS bloat_bytes "
        sql += " FROM estimates_with_toast "
        sql += " UNION ALL "
        sql += "     SELECT current_database() as databasename, "
        sql += " table_schema, table_name, FALSE, "
        sql += " est_rows, table_size, "
        sql += " NULL::NUMERIC, NULL::NUMERIC "
        sql += " FROM no_stats "
        sql += " ), "
        sql += " bloat_data AS ( "
        sql += " select current_database() as databasename, "
        sql += " schemaname, tablename, can_estimate, "
        sql += " table_bytes, round(table_bytes/(1024^2)::NUMERIC,3) as table_mb, "
        sql += " expected_bytes, round(expected_bytes/(1024^2)::NUMERIC,3) as expected_mb, "
        sql += " round(bloat_bytes*100/table_bytes) as pct_bloat, "
        sql += " round(bloat_bytes/(1024::NUMERIC^2),2) as mb_bloat, "
        sql += " table_bytes, expected_bytes, est_rows "
        sql += " FROM table_estimates_plus "
        sql += " ) "
        sql += " SELECT databasename, schemaname, tablename, "
        sql += " can_estimate, "
        sql += " est_rows, "
        sql += " pct_bloat, mb_bloat, "
        sql += " table_mb "
        sql += " FROM bloat_data "
        sql += " WHERE ( pct_bloat >= 50 AND mb_bloat >= 20 ) "
        sql += "     OR ( pct_bloat >= 25 AND mb_bloat >= 1000 ) "
        sql += " ORDER BY pct_bloat DESC;"
        
        
        
        cur.execute(sql)
        row = cur.fetchone()
        if row is not None:
            while row is not None:
                print(row)
                row = cur.fetchone()
              
        print (30 * '-')
        print ("   Bloating Report  - Index ")
        print (30 * '-')
        
        sql1 = " WITH btree_index_atts AS (  "
        sql1 += " SELECT nspname,   "
        sql1 += " indexclass.relname as index_name,   "
        sql1 += " indexclass.reltuples,   "
        sql1 += " indexclass.relpages,   "
        sql1 += " indrelid, indexrelid,  "
        sql1 += " indexclass.relam,  "
        sql1 += " tableclass.relname as tablename,  "
        sql1 += " regexp_split_to_table(indkey::text, ' ')::smallint AS attnum,  "
        sql1 += " indexrelid as index_oid  "
        sql1 += " FROM pg_index  "
        sql1 += " JOIN pg_class AS indexclass ON pg_index.indexrelid = indexclass.oid  "
        sql1 += " JOIN pg_class AS tableclass ON pg_index.indrelid = tableclass.oid  "
        sql1 += " JOIN pg_namespace ON pg_namespace.oid = indexclass.relnamespace  "
        sql1 += " JOIN pg_am ON indexclass.relam = pg_am.oid  "
        sql1 += " WHERE pg_am.amname = 'btree' and indexclass.relpages > 0  "
        sql1 += "  AND nspname NOT IN ('pg_catalog','information_schema')  "
        sql1 += " ),  "
        sql1 += " index_item_sizes AS (  "
        sql1 += " SELECT  "
        sql1 += " ind_atts.nspname, ind_atts.index_name,   "
        sql1 += " ind_atts.reltuples, ind_atts.relpages, ind_atts.relam,  "
        sql1 += " indrelid AS table_oid, index_oid,  "
        sql1 += " current_setting('block_size')::numeric AS bs,  "
        sql1 += " 8 AS maxalign,  "
        sql1 += " 24 AS pagehdr,  "
        sql1 += " CASE WHEN max(coalesce(pg_stats.null_frac,0)) = 0  "
        sql1 += " THEN 2  "
        sql1 += " ELSE 6  "
        sql1 += " END AS index_tuple_hdr,  "
        sql1 += " sum( (1-coalesce(pg_stats.null_frac, 0)) * coalesce(pg_stats.avg_width, 1024) ) AS nulldatawidth  "
        sql1 += " FROM pg_attribute  "
        sql1 += " JOIN btree_index_atts AS ind_atts ON pg_attribute.attrelid = ind_atts.indexrelid AND pg_attribute.attnum = ind_atts.attnum  "
        sql1 += " JOIN pg_stats ON pg_stats.schemaname = ind_atts.nspname  "
        sql1 += " -- stats for regular index columns  "
        sql1 += " AND ( (pg_stats.tablename = ind_atts.tablename AND pg_stats.attname = pg_catalog.pg_get_indexdef(pg_attribute.attrelid, pg_attribute.attnum, TRUE))   "
        sql1 += " -- stats for functional indexes  "
        sql1 += " OR   (pg_stats.tablename = ind_atts.index_name AND pg_stats.attname = pg_attribute.attname))  "
        sql1 += " WHERE pg_attribute.attnum > 0  "
        sql1 += " GROUP BY 1, 2, 3, 4, 5, 6, 7, 8, 9  "
        sql1 += " ),  "
        sql1 += " index_aligned_est AS (  "
        sql1 += " SELECT maxalign, bs, nspname, index_name, reltuples,  "
        sql1 += " relpages, relam, table_oid, index_oid,  "
        sql1 += " coalesce (  "
        sql1 += " ceil (  "
        sql1 += " reltuples * ( 6   "
        sql1 += " + maxalign   "
        sql1 += " - CASE  "
        sql1 += " WHEN index_tuple_hdr%maxalign = 0 THEN maxalign "
        sql1 += " ELSE index_tuple_hdr%maxalign "
        sql1 += "   END "
        sql1 += " + nulldatawidth  "
        sql1 += " + maxalign  "
        sql1 += " - CASE /* Add padding to the data to align on MAXALIGN */ "
        sql1 += " WHEN nulldatawidth::integer%maxalign = 0 THEN maxalign "
        sql1 += " ELSE nulldatawidth::integer%maxalign "
        sql1 += "   END "
        sql1 += " )::numeric  "
        sql1 += "   / ( bs - pagehdr::NUMERIC ) "
        sql1 += "   +1 ) "
        sql1 += "  , 0 ) "
        sql1 += "   as expected "
        sql1 += " FROM index_item_sizes "
        sql1 += " ), "
        sql1 += " raw_bloat AS ( "
        sql1 += " SELECT current_database() as dbname, nspname, pg_class.relname AS table_name, index_name, "
        sql1 += " bs*(index_aligned_est.relpages)::bigint AS totalbytes, expected, "
        sql1 += " CASE "
        sql1 += " WHEN index_aligned_est.relpages <= expected  "
        sql1 += " THEN 0 "
        sql1 += " ELSE bs*(index_aligned_est.relpages-expected)::bigint  "
        sql1 += " END AS wastedbytes, "
        sql1 += " CASE "
        sql1 += " WHEN index_aligned_est.relpages <= expected "
        sql1 += " THEN 0  "
        sql1 += " ELSE bs*(index_aligned_est.relpages-expected)::bigint * 100 / (bs*(index_aligned_est.relpages)::bigint)  "
        sql1 += " END AS realbloat, "
        sql1 += " pg_relation_size(index_aligned_est.table_oid) as table_bytes, "
        sql1 += " stat.idx_scan as index_scans "
        sql1 += " FROM index_aligned_est "
        sql1 += " JOIN pg_class ON pg_class.oid=index_aligned_est.table_oid "
        sql1 += " JOIN pg_stat_user_indexes AS stat ON index_aligned_est.index_oid = stat.indexrelid "
        sql1 += " ), "
        sql1 += " format_bloat AS ( "
        sql1 += " SELECT dbname as database_name, nspname as schema_name, table_name, index_name, "
        sql1 += " round(realbloat) as bloat_pct, round(wastedbytes/(1024^2)::NUMERIC) as bloat_mb, "
        sql1 += " round(totalbytes/(1024^2)::NUMERIC,3) as index_mb, "
        sql1 += " round(table_bytes/(1024^2)::NUMERIC,3) as table_mb, "
        sql1 += " index_scans "
        sql1 += " FROM raw_bloat "
        sql1 += " ) "
        sql1 += " SELECT * "
        sql1 += " FROM format_bloat "
        sql1 += " WHERE ( bloat_pct > 5 and bloat_mb > 10 ) "
        sql1 += " ORDER BY bloat_mb DESC; "

        cur.execute(sql1)
        row1 = cur.fetchone()
        if row1 is not None:
            while row is not None:
                print(row)
                row = cur.fetchone()
             
        if row is None or row1 is None:
            print("Database is Healthy")
            
            
        print("Press any key")
        char = getch.getch()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    #postgresmenu()

def databasevacuum():
    """
    Perform Database Vacuum
    
    """
    try:
        
        cur = conn.cursor()
        sql = "SELECT     datname     FROM     pg_database"
        cur.execute(sql)
        row = cur.fetchone()
        if row is not None:
            while row is not None:
                print(row[0])
            
                sql1 = " vacuumdb -v -d " + row[0]
                print (sql1)
                cur.execute(sql1)
                row = cur.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error =" , error)
    #print ("Database VACUUM !\n")
    return

def vacuumtable():
    """
    Perform Table Vacuum

    """
    try:
        
        cur = conn.cursor()
        sql = "SELECT     datname     FROM     pg_database"
        cur.execute(sql)
        row = cur.fetchone()
        if row is not None:
            while row is not None:
                print(row[0])
                
                sql1 = " vacuumdb -v -d " + row[0]
                print (sql1)
                cur.execute(sql1)
                row = cur.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error =", error)
    # print ("Database VACUUM !\n")

    return

def backupdatabase():
    print ("Backup Database !\n")
    return

def backuptable():
    print ("Backup Table !\n")
    return

def databasersync():
    print ("Database Resync Task !\n")
    return

def databaseanalyze():
    print ("Database Analyze !\n")
    return


def pgpoolstatus():
    print ("Pgpool Status !\n")
    
    print("Press any key")
    char = getch.getch()
    return

def noofpgpoolconnections():
    print ("No. Of Pgpool Connections !\n")

    print("Press any key")
    char = getch.getch()
    return

def nodestatus():
    print ("Database Node Status !\n")
    cur = pgconn.cursor()
    cur.execute('show pool_nodes')
    row = cur.fetchone()
    while row is not None:
        print(row)
        row = cur.fetchone()
    print("Press any key")
    char = getch.getch()
    return

def nodersync():
    print ("Node R-Sync !\n")

    print("Press any key")
    char = getch.getch()
    return


def databasereplicationstatus():
    # os.system('clear')
    """
    Function to display the status of Streaming Replication.

    """
    try:
        print (30 * '-')
        print ("  Replication Status   ")
        print (30 * '-')
        cur = conn.cursor()
        cur.execute('select * from pg_stat_replication')
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()

        print ("\n")
        print ("  Current WAL LSN    ")
        print (30 * '-')
        cur.execute('SELECT pg_current_wal_lsn() AS location')
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()

        print("Press any key")
        char = getch.getch()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    databasemainteiancetasks()


##Delete Later

def menu2():
    print ("MYSQL !\n")
    return
def menu3():
    print ("MYSQL !\n")
    return
def menu4():
    print ("MYSQL !\n")
    return

# =======================
#    MENUS DEFINITIONS
# =======================


# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': OracleConfiguration,
    '2': SQLServerConfiguration,
    '3': postgresConfiguration,
    '4': MysqlConfiguration,
    '0': exit,
}

menu_postgresactions = {
    'postgresmenu': postgresmenu,
    '1': noofconnections,
    '2': noofidleconnections,
    '3': menu3,
    '4': pgbloating,
    '5': pgblocking,
    '6': printdatabaseconfiguration,
    '7': databasereplicationstatus,
    '8': databasemainteiancetasks,
    '9': pgpoolMenu,
    '0': exit,
}

menu_databasemainteiancetasks = {
    'databasemainteiancetasks': databasemainteiancetasks,
    '1': databasevacuum,
    '2': vacuumtable,
    '3': backupdatabase,
    '4': backuptable,
    '5': databasersync,
    '6': databaseanalyze,
    '9': postgresmenu,
    '0': exit,
}

menu_pgpoolactions = {
    'pgpoolMenu': pgpoolMenu,
    '1': pgpoolstatus,
    '2': noofpgpoolconnections,
    '3': nodestatus,
    '4': nodersync,
    '6': pgpoolMenu,
    '0': exit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()