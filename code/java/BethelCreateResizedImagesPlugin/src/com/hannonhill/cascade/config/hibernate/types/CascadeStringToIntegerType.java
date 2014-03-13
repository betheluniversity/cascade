/*
 * Created on Feb 8, 2007 by Bradley Wagner
 * 
 * Copyright(c) 2000-2007 Hannon Hill Corporation.  All rights reserved.
 */
package com.hannonhill.cascade.config.hibernate.types;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Types;

import org.hibernate.dialect.Dialect;
import org.hibernate.type.StringType;

/**
 * Custom hibernate type that maps a Java {@link String}
 * to a SQL Integer
 * 
 * @author  Bradley Wagner
 * @version $Id$
 * @since   5.0
 */
public class CascadeStringToIntegerType extends StringType
{

    /** Serial version universal identifier */
    private static final long serialVersionUID = 9149503354361022318L;

    /* (non-Javadoc)
     * @see org.hibernate.type.StringType#get(java.sql.ResultSet, java.lang.String)
     */
    @Override
    public Object get(ResultSet rs, String name) throws SQLException
    {
        Integer intValue = rs.getInt(name);
        return intValue.toString();
    }

    /* (non-Javadoc)
     * @see org.hibernate.type.StringType#objectToSQLString(java.lang.Object, org.hibernate.dialect.Dialect)
     */
    @Override
    public String objectToSQLString(Object value, Dialect dialect) throws Exception
    {
        return (String) value;
    }

    /* (non-Javadoc)
     * @see org.hibernate.type.StringType#set(java.sql.PreparedStatement, java.lang.Object, int)
     */
    @Override
    public void set(PreparedStatement st, Object value, int index) throws SQLException
    {
        st.setInt(index, new Integer((String)value));
    }

    /* (non-Javadoc)
     * @see org.hibernate.type.StringType#sqlType()
     */
    @Override
    public int sqlType()
    {
        return Types.INTEGER;
    }    
}