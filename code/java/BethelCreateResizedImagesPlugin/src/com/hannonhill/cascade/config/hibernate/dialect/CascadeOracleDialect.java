/*
 * Created on Jul 9, 2007 by Nedko Hristov
 * 
 * Copyright(c) 2000-2007 Hannon Hill Corporation.  All rights reserved.
 */
package com.hannonhill.cascade.config.hibernate.dialect;

import java.sql.Types;

import org.hibernate.dialect.Oracle9iDialect;

/**
 * Default Oracle dialect for Cascade server takes a somewhat conservative approach.
 * Adjusts for the deprecated Oracle9Dialect since 3.2.5 of Hibernate
 * Our own version of the Oracle dialect so we have support for doubles in Hibernate
 * the type DOUBLE PRECISION is a synonym or rather alias of FLOAT(126) so we actually
 * want to tell hibernate to map it to float without any errors.
 * 
 * @author  Nedko Hristov
 * @version $Id$
 * @since   5.0
 */
public class CascadeOracleDialect extends Oracle9iDialect
{
    public CascadeOracleDialect()
    {
        super();
        //maps with Java double; In Oracle10 binary_double can be used (not backwards compatible)
        registerColumnType(Types.DOUBLE, "float");
    }
}
