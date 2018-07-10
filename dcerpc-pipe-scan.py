import time, sys
from impacket import uuid
from impacket.dcerpc.v5 import transport
from impacket.dcerpc.v5.rpcrt import DCERPCException

pipes ={
  ('atsvc','Scheduler service','mstask.exe','1ff70682-0a51-30e8-076d-740be8cee98b','1.0'),
  ('AudioSrv','Windows Audio service','AudioSrv','3faf4738-3a21-4307-b46c-fdda9bb8c0d5','1.0'),
  ('browser','Computer Browser','Browser','6bffd098-a112-3610-9833-012892020162','0.0'),
  ('cert','Certificate services','certsrv.exe','91ae6020-9e3c-11cf-8d7c-00aa00c091be','0.0'),
  ('Ctx_Winstation_API_Service','Terminal Services remote management','termsrv.exe','5ca4a760-ebb1-11cf-8611-00a0245420ed','1.0'),
  ('DAV RPC SERVICE','WebDAV client','WebClient','c8cb7687-e6d3-11d2-a958-00c04f682e16','1.0'),
  ('dnsserver','DNS Server','dns.exe','50abc2a4-574d-40b3-9d66-ee4fd5fba076','5.0'),
  ('epmapper','RPC endpoint mapper','RpcSs','e1af8308-5d1f-11c9-91a4-08002b14a0fa','3.0'),
  ('eventlog','EventLog Remoting Protocol','wevtsvc.dll','f6beaff7-1e19-4fbb-9f8f-b89e2018337c','1.0'),
  ('eventlog','Eventlog service','Eventlog','82273fdc-e32a-18c3-3f78-827929dc23ea','0.0'),
  ('HydraLsPipe','Terminal Server Licensing','lserver.exe','3d267954-eeb7-11d1-b94e-00c04fa3080d','1.0'),
  ('InitShutdown','(Remote) system shutdown','winlogon.exe','894de0c0-0d55-11d3-a322-00c04fa321a1','1.0'),
  ('keysvc','Cryptographic services','CryptSvc','8d0ffe72-d252-11d0-bf8f-00c04fd9126b','1.0'),
  ('keysvc','Cryptographic services','CryptSvc','0d72a7d4-6148-11d1-b4aa-00c04fb66ea0','1.0'),
  ('locator','RPC Locator service','locator.exe','d6d70ef0-0e3b-11cb-acc3-08002b1d29c4','1.0'),
  ('llsrpc','Licensing Logging service','llssrv.exe','342cfd40-3c6c-11ce-a893-08002b2e9c6d','0.0'),
  ('lsarpc','LSA access','lsass.exe','12345778-1234-abcd-ef00-0123456789ab','0.0'),
  ('lsarpc','LSA DS access','lsass.exe','3919286a-b10c-11d0-9ba8-00c04fd92ef5','0.0'),
  ('msgsvc','Messenger service','messenger','5a7b91f8-ff00-11d0-a9b2-00c04fb6e6fc','1.0'),
  ('netdfs','Distributed File System service','Dfssvc','4fc742e0-4a10-11cf-8273-00aa004ae673','3.0'),
  ('netlogon','Net Logon service','Netlogon','12345678-1234-abcd-ef00-01234567cffb','1.0'),
  ('ntsvcs','Plug and Play service','services.exe','8d9f4e40-a03d-11ce-8f69-08003e30051b','1.0'),
  ('policyagent','IPSEC Policy Agent (Windows 2000)','PolicyAgent','d335b8f6-cb31-11d0-b0f9-006097ba4e54','1.5'),
  ('ipsec','IPsec Services','PolicyAgent','12345678-1234-abcd-ef00-0123456789ab','1.0'),
  ('ProfMapApi','Userenv','winlogon.exe','369ce4f0-0fdc-11d3-bde8-00c04f8eee78','1.0'),
  ('protected_storage','Protected Storage','lsass.exe','c9378ff1-16f7-11d0-a0b2-00aa0061426a','1.0'),
  ('ROUTER','Remote Access','mprdim.dll','8f09f000-b7ed-11ce-bbd2-00001a181cad','0.0'),
  ('samr','SAM access','lsass.exe','12345778-1234-abcd-ef00-0123456789ac','1.0'),
  ('scerpc','Security Configuration Editor (SCE)','services.exe','93149ca2-973b-11d1-8c39-00c04fb984f9','0.0'),
  ('SECLOGON','Secondary logon service','seclogon','12b81e99-f207-4a4c-85d3-77b42f76fd14','1.0'),
  ('SfcApi','Windows File Protection','winlogon.exe','83da7c00-e84f-11d2-9807-00c04f8ec850','2.0'),
  ('spoolss','Spooler service','spoolsv.exe','12345678-1234-abcd-ef00-0123456789ab','1.0'),
  ('srvsvc','Server service','services.exe (w2k) or svchost.exe (wxp and w2k3)','4b324fc8-1670-01d3-1278-5a47bf6ee188','3.0'),
  ('ssdpsrv','SSDP service','ssdpsrv','4b112204-0e19-11d3-b42b-0000f81feb9f','1.0'),
  ('svcctl','Services control manager','services.exe','367aeb81-9844-35f1-ad32-98f038001003','2.0'),
  ('tapsrv','Telephony service','Tapisrv','2f5f6520-ca46-1067-b319-00dd010662da','1.0'),
  ('trkwks','Distributed Link Tracking Client','Trkwks','300f3532-38cc-11d0-a3f0-0020af6b0add','1.2'),
  ('W32TIME','Windows Time (Windows 2000 and XP)','w32time','8fb6d884-2388-11d0-8c35-00c04fda2795','4.1'),
  ('W32TIME_ALT','Windows Time (Windows Server 2003)','w32time','8fb6d884-2388-11d0-8c35-00c04fda2795','4.1'),
  ('winlogonrpc','Winlogon','winlogon.exe','a002b3a0-c9b7-11d1-ae88-0080c75e4ec1','1.0'),
  ('winreg','Remote registry service','RemoteRegistry','338cd001-2244-31f1-aaaa-900038001003','1.0'),
  ('winspipe','WINS service','wins.exe','45f52c28-7f9f-101a-b52b-08002b2efabe','1.0'),
  ('wkssvc','Workstation service','services.exe (w2k) or svchost.exe (wxp and w2k3)','6bffd098-a112-3610-9833-46c3f87e345a','1.0')
}

if len(sys.argv) != 3:
  print("Usage:")
  print("{} <ip> <port>".format(sys.argv[0]))
  sys.exit(1)

host, port = sys.argv[1],  int(sys.argv[2])

print "[*] dcerpc-pipe-scan 0.1"
print "[*] by p33kab00 (mudnorb@gmail.com)"
print "[*] # of checks: %i\n" %(len(pipes))

start = time.time()*1000
bnd = 0
for pipe in pipes:
  try:
    stringbinding = "ncacn_np:%s[\pipe\%s]" % (host,pipe[0])
    trans = transport.DCERPCTransportFactory(stringbinding)
    trans.set_dport(port)
    dce = trans.get_dce_rpc()
    dce.connect()
    dce.bind(uuid.uuidtup_to_bin((pipe[3],pipe[4])))
    print "[+] Found accessible endpoint"
    print "    %s" %(pipe[1])
    print "    Provider:\t%s (\PIPE\%s)" %(pipe[2],pipe[0])
    print "    UUID:\t%s v%s\n" %(pipe[3],pipe[4])
    bnd += 1
    dce.disconnect()
  except Exception as e:
    #print('{}: Nope').format(str(e))
    pass

stop = time.time()*1000
print "[*] Found %i possible bindings in %i ms." %(bnd, int(stop-start))

