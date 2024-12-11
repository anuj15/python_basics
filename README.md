Database Backup / Restore process high-level: 
Backup Full for Product (DMZ) Ready Database
Copy Full to US-West / Singapore / US-East 
Restore Full with NoRecovery Sync from FinancialPublish -> Product (DMZ) Ready Database
Backup Differential for Product (DMZ) Ready Database
Copy Differential to US-West / Singapore / US-East 
Restore Differential WITH Recovery Change Metadata / ObjectViews / etc. 
Test
