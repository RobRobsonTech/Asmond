description = [[
This script stores the following nmap output into a sqlite3 database: Hostname, IP, port number, protocol (tcp/udp), service and version
Both, database file name and table name can be passed to the script via arguments (see @args or @example), data will always be appended to an existing table. Non-existant database files or table
s are created during the scan. Nmap's regular output (-o) will not be modified in any way.

Dependencies: luasql (http://keplerproject.org/luasql)
]]

---
-- @usage
-- nmap --script sqlite-output <target>
--
-- @example
-- $ nmap -sS -A -F --script sqlite-output --script-args=dbname=scan.sqlite,dbtable=scandata scanme.nmap.org
-- $ sqlite3 can.sqlite
-- sqlite> select * from scandata;
-- scanme.nmap.org|74.207.244.221|22|tcp|ssh|OpenSSH5.3p1 Debian 3ubuntu7.1
-- scanme.nmap.org|74.207.244.221|80|tcp|http|Apache httpd2.2.14
--
-- @args
-- dbname:  name of sqlite database file (default: scan.sqlite)
-- dbtable: name of database table in which the output will be written (default: scandata)
---

author = "Michael Clemens"
license = "Same as Nmap--See http://nmap.org/book/man-legal.html"
categories = {"external", "safe"}

local luasql = require "luasql.sqlite3"
local nmap = require "nmap"

portrule = function () return true end
postrule = function () return true end

if (nmap.registry.args.dbname~=nil) then
        dbname = nmap.registry.args.dbname
else
        dbname = "scan.sqlite"
end

if (nmap.registry.args.dbtable~=nil) then
        dbtable = nmap.registry.args.dbtable
else
        dbtable = "scandata"
end

env = luasql.sqlite3()
con = env:connect(dbname)
res = con:execute (string.format("CREATE TABLE '%s' (hostname varchar(100), ip varchar(16), port integer(5), protocol varchar(3), state varchar(20), service varchar(100), version varchar(100))", con:escape(dbtable)))

function portaction (host, port)
        local version = ""
        if (port.version.product~=nil) then
                version = port.version.product
        end
        if (port.version.version~=nil) then
                version = version .. port.version.version
        end
        res = con:execute(string.format("INSERT INTO '%s' VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" , con:escape(dbtable), con:escape(host.name), con:escape(host.ip), con:escape(port.number), con:escape(port.protocol), con:escape(port.state), con:escape(port.service), con:escape(version)))

end

function postaction ()
        con:close()
        env:close()
end

local ActionsTable = {
  portrule = portaction,
  postrule = postaction
}

-- execute the action function corresponding to the current rule
action = function(...) return ActionsTable[SCRIPT_TYPE](...) end