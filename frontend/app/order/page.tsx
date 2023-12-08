'use client'

import React from 'react';
import {
  Box,
  Container,
  Link,
  Text,
  HStack,
  VStack,
  Flex,
  Icon,
  useColorModeValue
} from '@chakra-ui/react';
import PaginationButton from '../component/pagination'

const milestones = [
  {
    order_id: 1,
    product_id: 1,
    quantity: 1,
    status: "Order Status",
    price: 20000
  },
  {
    order_id: 1,
    product_id: 1,
    quantity: 1,
    status: "Order Status",
    price: 20000
  },
  {
    order_id: 1,
    product_id: 1,
    quantity: 1,
    status: "Order Status",
    price: 20000
  },
];

const Milestones = () => {
  return (
    <Container maxWidth="8xl" p={{ base: 2, sm: 10 }}>
      <Box fontSize="4xl" fontWeight="bold" mb={12} textAlign="center" color="white" bg="orange.400" h="20" py="3" w="full">
        Order
      </Box>
      <Box pb="2">
      {milestones.map((milestone, index) => (
        <Flex key={index} mb="10x">
          <LineWithDot />
          <Card {...milestone} />
        </Flex>
      ))}
      <Flex mt="5" mb="-5">
        <PaginationButton />
        </Flex>
        </Box>
    </Container>
  );
};

interface CardProps {
    order_id: number,
    product_id: number,
    quantity: number,
    status: string,
    price: number
}

const Card = ({ order_id, product_id, quantity, status, price}: CardProps) => {
  return (
    <HStack
      p={{ base: 4, sm: 6 }}
      spacing={2}
      rounded="lg"
      alignItems="center"
      pos="relative"
      _before={{
        content: `""`,
        w: '0',
        h: '0',
        borderColor: 'transparent',
        borderStyle: 'solid',
        borderWidth: '15px 15px 15px 0',
        position: 'absolute',
        left: '-15px',
        display: 'block',
      }}
    >
      <Icon w={12} h={12} color="orange.400" />
      <Box>
          <Box
            fontSize="2xl"
            lineHeight={1.2}
            fontWeight="bold"
            w="100%"
            pb="3"
          >
            Order: {order_id}
          </Box>
          <Text fontSize="md" pb="1">
            Product ID {product_id} - Quantity {quantity} - Rp{price}
          </Text>
        <Text fontSize="sm">{status}</Text>
      </Box>
    </HStack>
  );
};

const LineWithDot = () => {
  return (
    <Flex pos="relative" alignItems="center" mr="40px">
      <Box
        pos="absolute"
        left="50%"
        height="calc(100% + 10px)"
        border="1px solid"
        top="0px"
      ></Box>
      <Box pos="relative" p="10px">
        <Box
          pos="absolute"
          width="100%"
          height="100%"
          bottom="0"
          right="0"
          top="0"
          left="0"
          backgroundSize="cover"
          backgroundRepeat="no-repeat"
          backgroundPosition="center center"
          backgroundColor="orange.400"
          borderRadius="100px"
          backgroundImage="none"
          opacity={1}
        ></Box>
      </Box>
    </Flex>
  );
};

export default Milestones;