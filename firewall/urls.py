from django.conf.urls import url
import views

urlpatterns = [
    url(r'^securityHome', views.securityHome, name='securityHome'),
    url(r'^$', views.firewallHome, name='firewallHome'),
    url(r'^getCurrentRules', views.getCurrentRules, name='getCurrentRules'),
    url(r'^addRule', views.addRule, name='addRule'),
    url(r'^deleteRule', views.deleteRule, name='deleteRule'),


    url(r'^reloadFirewall', views.reloadFirewall, name='reloadFirewall'),
    url(r'^stopFirewall', views.stopFirewall, name='stopFirewall'),
    url(r'^startFirewall', views.startFirewall, name='startFirewall'),
    url(r'^firewallStatus', views.firewallStatus, name='firewallStatus'),

    ## secure SSH

    url(r'^secureSSH', views.secureSSH, name='secureSSH'),
    url(r'^getSSHConfigs', views.getSSHConfigs, name='getSSHConfigs'),
    url(r'^saveSSHConfigs', views.saveSSHConfigs, name='saveSSHConfigs'),
    url(r'^deleteSSHKey', views.deleteSSHKey, name='deleteSSHKey'),
    url(r'^addSSHKey', views.addSSHKey, name='addSSHKey'),


    ## ModSecurity

    url(r'^modSecurity', views.loadModSecurityHome, name='modSecurity'),
    url(r'^installModSec$', views.installModSec, name='installModSec'),
    url(r'^installStatusModSec$', views.installStatusModSec, name='installStatusModSec'),
    url(r'^fetchModSecSettings', views.fetchModSecSettings, name='fetchModSecSettings'),
    url(r'^saveModSecConfigurations', views.saveModSecConfigurations, name='saveModSecConfigurations'),
    url(r'^modSecRules$', views.modSecRules, name='modSecRules'),
    url(r'^fetchModSecRules', views.fetchModSecRules, name='fetchModSecRules'),
    url(r'^saveModSecRules', views.saveModSecRules, name='saveModSecRules'),
    url(r'^modSecRulesPacks', views.modSecRulesPacks, name='modSecRulesPacks'),
    url(r'^getOWASPAndComodoStatus', views.getOWASPAndComodoStatus, name='getOWASPAndComodoStatus'),
    url(r'^installModSecRulesPack', views.installModSecRulesPack, name='installModSecRulesPack'),
    url(r'^getRulesFiles', views.getRulesFiles, name='getRulesFiles'),
    url(r'^enableDisableRuleFile', views.enableDisableRuleFile, name='enableDisableRuleFile'),



]