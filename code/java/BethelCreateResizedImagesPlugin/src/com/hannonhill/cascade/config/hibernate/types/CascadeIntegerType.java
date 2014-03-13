/*
 * Created on Mar 23, 2007 by Zach Bailey
 *
 * Copyright(c) 2007 Hannon Hill Corporation. All rights reserved.
 */
package com.hannonhill.cascade.config.hibernate.types;

import java.sql.Types;

import org.hibernate.type.IntegerType;

/**
 * Maps an integer (Integer or int field) to 
 * a tinyint database column.
 * 
 * This is used for mapping version columns for instance.
 * 
 * @author Zach Bailey
 * @since  5.0
 * @version $Id$
 */
public class CascadeIntegerType extends IntegerType
{
    private static final long serialVersionUID = -7693370814236396031L;

    /* (non-Javadoc)
     * @see org.hibernate.type.IntegerType#sqlType()
     */
    @Override
    public int sqlType()
    {
        return Types.TINYINT;
    }
}
