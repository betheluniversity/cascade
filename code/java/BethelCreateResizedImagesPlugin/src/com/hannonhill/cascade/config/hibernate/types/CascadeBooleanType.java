/*
 * Created on Feb 6, 2007 by Bradley Wagner
 * 
 * Copyright(c) 2000-2007 Hannon Hill Corporation.  All rights reserved.
 */
package com.hannonhill.cascade.config.hibernate.types;

import java.sql.Types;

import org.hibernate.type.BooleanType;
import org.hibernate.usertype.UserType;

/**
 * Implementation of the Hibernate {@link UserType}
 * for Cascade's booleans which map to integers in
 * our existing table schemas
 * 
 * @author  Bradley Wagner
 * @version $Id$
 * @since   5.0
 */
public class CascadeBooleanType extends BooleanType
{

    /** serial vesion universal identifier */
    private static final long serialVersionUID = 1028648325077618086L;

    /**
     * Public constructor
     */
    public CascadeBooleanType()
    {

    }

    /* (non-Javadoc)
     * @see org.hibernate.type.BooleanType#sqlType()
     */
    @Override
    public int sqlType()
    {
        return Types.TINYINT;
    }
}
