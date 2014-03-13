/*
 * Created on Mar 27, 2007 by Zach Bailey
 *
 * Copyright(c) 2007 Hannon Hill Corporation. All rights reserved.
 */
package com.hannonhill.cascade.config.hibernate.dialect;

import org.hibernate.LockMode;
import org.hibernate.dialect.SQLServerDialect;

/**
 * Cascade custom dialect for use with Hibernate on SQL Server.
 * 
 * As of the current revision, we support SQL Server 2005 and 2008.
 * 
 * @author  Zach Bailey
 * @version $Id$
 * @since   5.0
 */
public class CascadeSQLServerDialect extends SQLServerDialect
{
    /* (non-Javadoc)
     * @see org.hibernate.dialect.Dialect#supportsUnionAll()
     */
    @Override
    public boolean supportsUnionAll()
    {
        // SQL Server 2005, 2008 support the UNION ALL operator. We no longer support 2000.
        // 2008 - http://msdn.microsoft.com/en-us/library/ms180026.aspx
        // 2005 - http://msdn.microsoft.com/en-us/library/ms180026%28SQL.90%29.aspx
        return true;
    }

    /* (non-Javadoc)
     * @see org.hibernate.dialect.SQLServerDialect#appendLockHint(org.hibernate.LockMode, java.lang.String)
     */
    @Override
    public String appendLockHint(LockMode mode, String tableName)
    {
        return super.appendLockHint(mode, tableName);

        /*
         * The following was suggested by Zach Bailey
         * 
        if (mode.greaterThan(LockMode.READ))
        {
            // does this need holdlock also? : return tableName + " with (updlock, rowlock, holdlock)";
            return tableName + " with (updlock, rowlock)";
        }
        else
        {
            return tableName + " with (nolock)";
        }
        */
    }
}
